from rest_framework.pagination import PageNumberPagination

# created custom paginator
class MyCustomPaginator(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 1000
    
    # if this is defined ordering will NOT WORK !!
    # def paginate_queryset(self, queryset, request, view=None):
    #     ordering = 'id' 
    #     queryset = queryset.order_by(ordering)
    #     return super().paginate_queryset(queryset, request, view)
