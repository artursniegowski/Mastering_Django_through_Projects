from django_filters import FilterSet, NumberFilter, CharFilter
from .models import MenuItem

class MenuItemFilter(FilterSet):
    category__title = CharFilter(field_name='category__title',lookup_expr='icontains')
    min_price = NumberFilter(field_name='price',lookup_expr='gte')
    max_price = NumberFilter(field_name='price',lookup_expr='lte')
    
    class Meta:
        model = MenuItem
        fields = ['category__title','min_price', 'max_price']
        # you can only use atributes that were defined in the model !
        # fields = {
        #     'category__title': ['icontains'], # make it case insensitive
        #     # 'min_price': ['gte'], 
        #     # 'max_price': ['lte'],
        # }