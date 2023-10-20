from django.db import models
from django.contrib.auth.models import User, Group
 
# Create your models here.
class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)
     
    def __str__(self) -> str:
        return self.title

class MenuItem(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    # menuitem will always belong to a category this is why we have one to many realtionship
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    
    def __str__(self) -> str:
        return self.title
     
class Cart(models.Model):
    # this is temporary storage for users that can add menu items before placing an order
    # a user can have only one cart at a time - this is why we need a reference to the user model
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    # this would be the unit price of the menu_item
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    # multiplies the quantity by the unit price for easier calulations
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        # for uniqe indexes, so menuitem and user have to be in the whole table unique
        # this means that there can we only one menuitem entry for a specific user 
        unique_together = ('menuitem', 'user')

class Order(models.Model):
    # linking the user table as a foreign key
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # in django you cant create two foreign keys refering to the same field in a foreign table
    # you must set a related name for it
    # bc both user and delivery_crew will referencing the user id
    delivery_crew = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='delivery_crew', null=True)
    # to mark if order is deliverd or not
    status = models.BooleanField(db_index=True, default=0)
    # total price of all the items in this order
    total = models.DecimalField(max_digits=6, decimal_places=2)
    # when was the order placed
    date = models.DateField(db_index=True)
    
class OrderItem(models.Model):
    # as soon as an order is placeed all the items will move from the cart to an order Item table 
    # and link those main items with the order ID, and then the cart items will be deleted
    # so after placing the order the cart will be empty and the user can start adding new items for a new order
    # it makes more sense if the relationship is to Order, this way we can refer
    # to any OrderItem by knowing the order
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    # this is for easier calulation and will be quantity time unit_price
    price = models.DecimalField(max_digits=6, decimal_places=2)
    
    class Meta:
        # for uniqe indexes, so order and menuitem have to be in the whole table unique
        # this means that one order can have only one entry for specific menuitem but qunatity can vary 
        unique_together = ('order', 'menuitem')
    
