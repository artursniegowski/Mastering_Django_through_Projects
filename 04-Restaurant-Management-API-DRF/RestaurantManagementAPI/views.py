from django.http import HttpRequest, HttpResponse
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.generics import ListCreateAPIView, DestroyAPIView
from rest_framework.response import Response
from .serializers import MenuItemSerializer, UserSerializerGET, UserSerializerPOST, CategorySerializer, CartSerializer, OrderSerializer, OrderDeliveryCrewSerializer, OrderManagerSerializer
from .models import MenuItem, User, Group, Category, Cart, Order
from .permissions import ManagersOnlyPermission, CustomersOnlyPermission, DeliveryCrewOnlyPermission
## for throttling
# they are set by default in the settings.py file on all the class base views
# so when you set the DEFAULT_THROTTLE_CLASSES in your settings.py, then all class based views 
# will get added the throttle_class = [AnonRateThrottle, UserRateThrottle]
# bc this is what it is specified in the settings.py
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
## pagination was only applied as per instruction for 
# these three endpoints:
# /api/menu-items
# /api/categories
# /api/orders
# to apply pagination for all endpoints we would have to configure the settings.py
# otherwise we apply the paginatin only fro these views
# from rest_framework.pagination import PageNumberPagination
# custom paginator:
from .pagination import MyCustomPaginator
# for filtering
from django_filters.rest_framework import DjangoFilterBackend
from .filters import MenuItemFilter
# for search filters
from rest_framework import filters

# Create your views here.
class MenuItemViewSet(viewsets.ModelViewSet):
    """handles the menu-item endpoint 
    """
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_class = MenuItemFilter
    # or use filterset_fields  
    # filterset_fields = {
    #     'category__title': ['icontains'], # make it case insensitive
    #     'price': ['gte', 'lte'], 
    # }
    # filterset_fields = ['category__title','price']
    search_fields = ['title', 'category__title']
    ordering_fields = ['price']
    
    # adding pagination for endpoint # /api/menu-items
    pagination_class = MyCustomPaginator
    # set already by default in settings.py - no need to defined it - only if you want to overide it !
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
    # default permissions
    # allows authenticated users to perform any CRUD operations, but only allows unauthenticated users to perform read-only operations.
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    # customizing permissions based on the groups,
    # only Managers can perform such actions as 'create', 'update', 'partial_update', 'destroy'
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # only for managers that are authenticated or admin users
            self.permission_classes = [IsAuthenticated & (ManagersOnlyPermission | IsAdminUser)]
        return super().get_permissions()
    
    
class CategoryViewSet(viewsets.ModelViewSet):
    """handles the categories endpoint"""
    # adding pagination for endpoint # /api/menu-items
    # pagination_class = MyCustomPaginator
    # set already by default in settings.py - no need to defined it - only if you want to overide it !
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    queryset = Category.objects.all()
    serializer_class = CategorySerializer 
    permission_classes = [IsAuthenticatedOrReadOnly] 
    
    # customizing permissions based on the groups,
    # only Managers can perform such actions as 'create', 'update', 'partial_update', 'destroy'
    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            # only for managers that are authenticated or admin users
            self.permission_classes = [IsAuthenticated & (ManagersOnlyPermission | IsAdminUser)]
        return super().get_permissions()
    
    
class ManagerUsersAPIView(ListCreateAPIView):
    """handles the adding and listing of managers"""
    # set already by default in settings.py - no need to defined it - only if you want to overide it !
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # only for managers that are authenticated or admin users
    permission_classes = [IsAuthenticated & (ManagersOnlyPermission | IsAdminUser)]
    # serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializerGET
        elif self.request.method == 'POST':
            return UserSerializerPOST
        else:
            return UserSerializerGET
    
    def get_queryset(self):
        # the django user model has a realtionship many to many with Group
        return User.objects.filter(groups__name='Manager')
  
    # adding the user to the manager group
    def create(self, request, *args, **kwargs):
        # getting the username
        username = request.data.get('username',None)
        
        # if username defined in the request
        if username:
            try: 
                # get the user instance if it exists
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({"message":"error, 'username' does not exists."}, status.HTTP_404_NOT_FOUND)
            else:
                # if user found we add the user to the manger group
                manager_group = Group.objects.get(name='Manager')
                manager_group.user_set.add(user)
                
                serializer = UserSerializerGET(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        # if username not provided
        return Response({"message":"error, 'username' was not provided in the request body."}, status.HTTP_400_BAD_REQUEST)
        
        
class ManagerUserDeleteAPIView(DestroyAPIView):
    """handles the deleting of managers"""
    # set already by default in settings.py - no need to defined it - only if you want to overide it !
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # only for managers that are authenticated or admin users
    permission_classes = [IsAuthenticated & (ManagersOnlyPermission | IsAdminUser)]
    serializer_class = UserSerializerPOST
    
    def destroy(self, request, *args, **kwargs):
        
        # getting the user_id
        user_id = kwargs.get('user_id',None)
        
        # if username defined in the request
        if user_id:
            try: 
                # get the user instance if it exists
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"message":"error, 'username' does not exists."}, status.HTTP_404_NOT_FOUND)
            else:
                # if user found and exists in the manager group
                if user.groups.filter(name='Manager').exists():
                    # removing user from the manger group
                    manager_group = Group.objects.get(name='Manager')
                    manager_group.user_set.remove(user)
                    
                    serializer = UserSerializerGET(user)
                    return Response({"message":f"success, user ({user.username}) was removed from Manager group."}, status=status.HTTP_200_OK)
                    # return Response(status=status.HTTP_204_NO_CONTENT)
                    # return Response(serializer.data, status=status.HTTP_200_OK)
                else :
                    return Response({"message":"error, user is not a manager."}, status=status.HTTP_400_BAD_REQUEST)
                    
        # if username not provided
        return Response({"message":"error, 'user_id' was not provided in the url."}, status.HTTP_400_BAD_REQUEST)
        
class DeliveryCrewUsersAPIView(ListCreateAPIView):
    """handles the adding and listing of Delivery - Crew"""
    # only for managers that are authenticated or admin users
    permission_classes = [IsAuthenticated & (ManagersOnlyPermission | IsAdminUser)]
    # serializer_class = UserSerializer
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return UserSerializerGET
        elif self.request.method == 'POST':
            return UserSerializerPOST
        else:
            return UserSerializerGET
    
    def get_queryset(self):
        # the django user model has a realtionship many to many with Group
        return User.objects.filter(groups__name='Delivery_Crew')
  
    # adding the user to the manager group
    def create(self, request, *args, **kwargs):
        # getting the username
        username = request.data.get('username',None)
        
        # if username defined in the request
        if username:
            try: 
                # get the user instance if it exists
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return Response({"message":"error, 'username' does not exists."}, status.HTTP_404_NOT_FOUND)
            else:
                # if user found we add the user to the Delivery_Crew group
                manager_group = Group.objects.get(name='Delivery_Crew')
                manager_group.user_set.add(user)
                
                serializer = UserSerializerGET(user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
                
        # if username not provided
        return Response({"message":"error, 'username' was not provided in the request body."}, status.HTTP_400_BAD_REQUEST)
        
        
class DeliveryCrewDeleteAPIView(DestroyAPIView):
    """handles the deleting of Delivery - Crew"""
    # set already by default in settings.py - no need to defined it - only if you want to overide it !
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # only for managers that are authenticated or admin users
    permission_classes = [IsAuthenticated & (ManagersOnlyPermission | IsAdminUser)]
    serializer_class = UserSerializerPOST
    
    def destroy(self, request, *args, **kwargs):
        
        # getting the user_id
        user_id = kwargs.get('user_id',None)
        
        # if username defined in the request
        if user_id:
            try: 
                # get the user instance if it exists
                user = User.objects.get(id=user_id)
            except User.DoesNotExist:
                return Response({"message":"error, 'username' does not exists."}, status.HTTP_404_NOT_FOUND)
            else:
                # if user found and exists in the Delivery_Crew group
                if user.groups.filter(name='Delivery_Crew').exists():
                    # removing user from the manger group
                    manager_group = Group.objects.get(name='Delivery_Crew')
                    manager_group.user_set.remove(user)
                    
                    serializer = UserSerializerGET(user)
                    return Response({"message":f"success, user ({user.username}) was removed from Delivery Crew group."}, status=status.HTTP_200_OK)
                    # return Response(status=status.HTTP_204_NO_CONTENT)
                    # return Response(serializer.data, status=status.HTTP_200_OK)
                else :
                    return Response({"message":"error, user is not in Delivery Crew."}, status=status.HTTP_400_BAD_REQUEST)
                    
        # if username not provided
        return Response({"message":"error, 'user_id' was not provided in the url."}, status.HTTP_400_BAD_REQUEST)
    
    
class CartAPIView(ListCreateAPIView):
    """handless the post, get and delete of cart items"""
    # set already by default in settings.py - no need to defined it - only if you want to overide it !
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    permission_classes = [IsAuthenticated & CustomersOnlyPermission]
    serializer_class = CartSerializer
    
    def get_queryset(self):
        # return the cart object that belong to the current user from the request
        current_user = self.request.user
        return Cart.objects.filter(user=current_user)
    
    # defining additional delete method for the endpoint
    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        if queryset.exists():
            queryset.delete()
            return Response({'message': 'All items have been removed from the cart.'})
        else:
            # TODO: which status code to send here ?? 
            return Response({'message': 'Cart is already empty.'})
            
                    
class OrderViewSet(viewsets.ModelViewSet):
    """handles the orders endpoint 
    """
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status']
    search_fields = ['user__username', 'delivery_crew__username']
    ordering_fields = ['date', 'total']
    
    # adding pagination for endpoint # /api/menu-items
    pagination_class = MyCustomPaginator
    # set already by default in settings.py - no need to defined it - only if you want to overide it !
    # throttle_classes = [AnonRateThrottle, UserRateThrottle]
    # default permissions
    # allows authenticated users to perform any CRUD operations
    permission_classes = [IsAuthenticated]
    
    # overiding the serilizer class
    def get_serializer_class(self):
        current_user = self.request.user 
        # for managers put/patch request
        if self.request.method in ['PUT','PATCH'] and current_user.groups.filter(name='Manager').exists():
            return OrderManagerSerializer
        # for delivery crew patch request
        elif self.request.method == 'PATCH' and current_user.groups.filter(name='Delivery_Crew').exists():
            return OrderDeliveryCrewSerializer
        # for all the other cases - default 
        else:
            return OrderSerializer
    
    # returning different query sets depending on the user group
    def get_queryset(self):
        current_user = self.request.user 
        # for managers - Returns all orders with order items by all users
        if current_user.groups.filter(name='Manager').exists():
            return Order.objects.all()
        # for delivery crew - Returns all orders with order items assigned to the delivery crew
        elif current_user.groups.filter(name='Delivery_Crew').exists():
            # TODO: delivery crew can be filtered diferently 
            
            # exlude all orders where the delivery_crew was not set yet - delivery crew would see all orders asigned to delivery crew
            # return Order.objects.exclude(delivery_crew=None)
            # asigned to the delivery crew user - will only see orders asigned to them
            return Order.objects.filter(delivery_crew=current_user)
        # for customers - Returns all orders with order items created by this user
        else:
            return Order.objects.filter(user=current_user)

    # customizing permissions based on the groups,
    # for actions as 'list', 'create', 'retrieve','update', 'partial_update', 'destroy'
    def get_permissions(self):
        if self.action in ['destroy', 'update']:
            # only for managers that are authenticated
            self.permission_classes = [IsAuthenticated & ManagersOnlyPermission]
        if self.action in ['create', 'retrieve']:
            # only for customers that are authenticated
            self.permission_classes = [IsAuthenticated & CustomersOnlyPermission]
        if self.action in ['partial_update']:
            # only for customers or managers that are authenticated
            self.permission_classes = [IsAuthenticated & (ManagersOnlyPermission | DeliveryCrewOnlyPermission)]
        
        return super().get_permissions()
    
    
# main page view fro the API           
def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("<h1>Welcome to the Restaurant Management API.</h1><p>Read the readme file first to understand which endpoints are accessible.<p>")