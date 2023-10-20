from rest_framework import serializers
from rest_framework.validators import UniqueValidator, UniqueTogetherValidator
from .models import Category, MenuItem, User, Cart, Order, OrderItem
from django.utils import timezone
from django.db import transaction

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category 
        fields = ['id','slug', 'title']

class MenuItemSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(
        queryset = Category.objects.all(),
    )
    
    # making sure that title is unique
    title = serializers.CharField(
        max_length=255,
        validators = [
            UniqueValidator(
                queryset= MenuItem.objects.all(),
                message='Menu item with this title already exists.',
            ),
        ]
    )

    class Meta:
        model = MenuItem
        fields = ['id','title','price', 'category', 'featured']
        
        # extra validation to make sure the featured is a boolean value
        def validate_featured(self, value):
            if not isinstance(value, bool):
                raise serializers.ValidationError("The 'featured' field must be a boolean value.")
            return value
    
        # contaianing the min values for the price
        extra_kwargs = {
            'price':{'min_value':2.00},
        }
        
class UserSerializerGET(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id','email','username']
        
class UserSerializerPOST(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']
        
        
class CartSerializer(serializers.ModelSerializer):
    price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    menuitem = serializers.PrimaryKeyRelatedField(
        queryset = MenuItem.objects.all(),
    )
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2, read_only=True)
    
    class Meta:
        model = Cart
        fields = ['id','user','menuitem','quantity','unit_price','price']

        extra_kwargs = {
            'quantity':{'min_value':1},
            'unit_price':{'min_value':1.0},
            'price':{'min_value':1.0},
        }
        
    # set the unit price as the MenuItem.price
    def get_unit_price(self, obj: Cart):
        return obj.menuitem.price
    
    # to save the calulated price to the model Cart
    # this could be also done in the models.py
    def create(self, validated_data):
        # getting the user from the request
        user = self.context['request'].user
        # set the user in the validated data 
        validated_data['user'] = user
        
        # checking for the unique togther of the combination of user and menuitem
        # it is kind of validation like UniqueTogetherValidator 
        # but since i cant implement it in the meta class bc at that time the user
        # dosent exists yet, the check will be perfomed here
        if Cart.objects.filter(user=user, menuitem=validated_data['menuitem']).exists():
            raise serializers.ValidationError({'menuitem': 'This menu item is already in the cart.'})
        
        # setting the unit_price from the menu_item
        validated_data['unit_price'] = validated_data['menuitem'].price
        
        # calcualte the price based on the quantity and unit price
        quantity = validated_data['quantity']
        unit_price = validated_data['unit_price']
        validated_data['price'] = quantity * unit_price
        cart = Cart.objects.create(**validated_data)

        return cart
    
class OrderItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','menuitem', 'unit_price', 'quantity', 'price']
        
        extra_kwargs = {
            'quantity':{'min_value':1},
            'unit_price':{'min_value':1.0},
            'price':{'min_value':1.0},
        }

## ORDER serializers
class OrderBaseSerializer(serializers.ModelSerializer):
    """base serilizer for Order"""
    user = serializers.PrimaryKeyRelatedField(read_only = True)
    delivery_crew = serializers.PrimaryKeyRelatedField(read_only = True)
    order_items  = serializers.SerializerMethodField()
    date = serializers.DateField()
    
    class Meta:
        model = Order
        fields = ['id','user','delivery_crew','status','total','date','order_items']
        read_only_fields = ['status','total']    

    def get_order_items(self, obj: Order):
        order_items = obj.orderitem_set.all() # getting all related order_items for this order - reverse relationship
        return OrderItemsSerializer(order_items, many=True).data
    
    
class OrderSerializer(OrderBaseSerializer):

    # for the POST request
    def create(self, validated_data):
        order = []
        with transaction.atomic():
            # get current cart imtes from the cart endpoint
            current_user = self.context['request'].user
            cart_items = Cart.objects.filter(user=current_user)
            
            # if there are no elements in the cart than raise a validation error
            if not cart_items.exists():
                raise serializers.ValidationError(
                    {'error': 'You cant place an order with an empty cart.',
                     'info': 'try adding menuitems at this endpoint first: /api/cart/menu-items'}
                    )
                
            # create new order
            order = Order.objects.create(
                user = current_user,
                # this has to be done by the manager
                # delivery_crew = # delivery crew wont be assing at the start
                # status = 0, # status wont be asigned at the beginign
                total = 0,
                date = validated_data['date'],
                # date = timezone.now().date(),
            )
            
            # now we create OrderItems based on the cart_items retrived
            total = 0
            order_items = []
            # coppying cart items
            for cart_item in cart_items:
                order_item = OrderItem.objects.create(
                    order = order,
                    menuitem = cart_item.menuitem,
                    quantity = cart_item.quantity,
                    unit_price = cart_item.unit_price,
                    price = cart_item.price
                )
                order_items.append(order_item)
                total += cart_item.price
    
            # delete cart items after creating order items
            cart_items.delete()

            # updating the total value for the order
            order.total = total
            order.save()
            
        return order
    
    
class OrderManagerSerializer(OrderBaseSerializer):
    delivery_crew = serializers.PrimaryKeyRelatedField(
        queryset = User.objects.filter(groups__name='Delivery_Crew'),
    )
    # overiding the date field to mek it read only
    date = serializers.DateField(read_only=True)
    status = serializers.BooleanField()
    
    class Meta(OrderBaseSerializer.Meta):
        read_only_fields = ['total']
        
    # extra validation to make sure the status is a boolean value
    def validate_status(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("The 'status' field must be a boolean value.")
        return value
    
    # this validation is not necessary bc the query set for delivery_crew takes into account only deliery crew users !
    def validate_delivery_crew(self, value):
        if not value.groups.filter(name='Delivery_Crew').exists():
            raise serializers.ValidationError("The 'delivery_crew' user must be part of the delivery crew group.")
        return value


class OrderDeliveryCrewSerializer(OrderBaseSerializer):
    # overiding the date field to mek it read only
    date = serializers.DateField(read_only=True)
    
    class Meta(OrderBaseSerializer.Meta):
        read_only_fields = ['total']
        
    # extra validation to make sure the status is a boolean value
    def validate_status(self, value):
        if not isinstance(value, bool):
            raise serializers.ValidationError("The 'status' field must be a boolean value.")
        return value
