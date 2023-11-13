from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

# ex: api/
# this will generate such routes as
# GET: /api/menu-items
# POST: /api/menu-items
# GET: /api/menu-items/{pk}
# PUT: /api/menu-items/{pk}
# PATCH: /api/menu-items/{pk}
# DELETE: /api/menu-items/{pk}
menu_item_routes = SimpleRouter(trailing_slash=False)
menu_item_routes.register('menu-items', views.MenuItemViewSet, basename='menu-items')


# ex: api/
# this will generate the endpoitn for upadting a creating categories
# GET: /api/categories
# POST: /api/categories
# DELETE: /api/categories/{pk}
# GET: /api/categories/{pk}
# PUT: /api/categories/{pk}
# PATCH: /api/categories/{pk}
# DELETE: /api/categories/{pk}
categories_routes = SimpleRouter(trailing_slash=False)
categories_routes.register('categories', views.CategoryViewSet, basename='categories')


# ex: api/
# this will generate the endpoitn for Order management
# GET: /api/orders
# POST: /api/orders
# DELETE: /api/orders/{pk}
# GET: /api/orders/{pk}
# PUT: /api/orders/{pk}
# PATCH: /api/orders/{pk}
# DELETE: /api/orders/{pk}
orders_routes = SimpleRouter(trailing_slash=False)
orders_routes.register('orders', views.OrderViewSet, basename='orders')


urlpatterns = [
    # ex: api/
    path('', views.index),
    # ex: api/
    path('', include(menu_item_routes.urls)),
    # ex: api/
    path('', include(categories_routes.urls)),
    # ex: api/
    path('', include(orders_routes.urls)),
    # ex: api/
    # api/cart
    # so here will be all # /api/cart/orders # endpoints
    # added aditional endpoints - is equivalent to api/orders
    path('cart/', include(orders_routes.urls)),
    # ex: api/
    # GET: /api/groups/manager/users
    # POST: /api/groups/manager/users
    path('groups/manager/users', views.ManagerUsersAPIView.as_view(),  name='manager-users'),
    # ex: api/
    # DELETE: /api/groups/manager/users/{pk}
    path('groups/manager/users/<int:user_id>', views.ManagerUserDeleteAPIView.as_view(),  name='manager-users-delete'),
     # ex: api/
    # GET: /api/groups/delivery-crew/users
    # POST: /api/groups/delivery-crew/users
    path('groups/delivery-crew/users', views.DeliveryCrewUsersAPIView.as_view(),  name='delivery-crew-users'),
    # ex: api/
    # DELETE: /api/groups/delivery-crew/users/{pk}
    path('groups/delivery-crew/users/<int:user_id>', views.DeliveryCrewDeleteAPIView.as_view(),  name='delivery-crew-users-delete'),
    # ex: api/
    # GET: /api/cart/menu-items
    # POST: /api/cart/menu-items
    # DELETE: /api/cart/menu-items
    path('cart/menu-items', views.CartAPIView.as_view(),  name='cart'),
    
] 
