from app_clients.models import Client
from app_users.models import User
from django.contrib import admin


class UsersInline(admin.TabularInline):
    model = User
    fields = ['username', 'email', 'date_joined', 'last_login' ]
    readonly_fields = [ 'username', 'email', 'date_joined', 'last_login' ]  

    extra = 0
    # if link required back to the booking 
    # show_change_link = True
    can_delete = False
    # if collapsed functionality of bookings required
    classes = ('collapse',)
    
    def has_add_permission(self, request, obj):
        return False


class ClientAdmin(admin.ModelAdmin):
    list_display = ['company','name']
    fields = ['company','name', 'descritpion']
    
    # specify the inlines
    inlines = [UsersInline]
    
    # include extra css to hide the title of the inline element
    class Media:
        css = {
            # for hiding the titel in the inline tabular
            'all':('css/custom_admin.css',)
        }


admin.site.register(Client,ClientAdmin)