from django.contrib import admin
from .models import Category, MenuItem, Cart, Order, OrderItem

# Register your models here.
class MenuItemInline(admin.StackedInline):
    model = MenuItem
    extra = 3
    
class CategoryAdmin(admin.ModelAdmin):
    inlines = [MenuItemInline]
    
admin.site.register(Category, CategoryAdmin)
admin.site.register(MenuItem)

# admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(OrderItem)