from app_funding.models import Project, Booking, Follower, Token
from django.contrib import admin
from django.http.request import HttpRequest
from django.urls import reverse
from django.utils import timezone
from django.utils.html import format_html
from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Type, Union

class FollowerInline(admin.TabularInline):
    model = Follower
    readonly_fields = ['display_linked_client', 'user','project','following_since_formated','button_book_request','book_request_date_formated']
    fields = ['display_linked_client', 'user','project','following_since_formated','button_book_request','book_request_date_formated']
    extra = 0
    can_delete = False
    # classes = ('collapse',)
    
    def button_book_request(self, obj):
        follower_id = obj.id 
        url = reverse('app_funding:booking-request',args=[follower_id])
        return format_html('<button type="button" class="bookRequestButton reactivateButton" data-url="{}">Booking Request</button>', url)
    button_book_request.short_description = 'Booking Request'
    
    def book_request_date_formated(self, obj):
        if not obj.book_request_date:
            return '-'
        return timezone.localtime(obj.book_request_date).strftime('%d-%m-%Y %H:%M:%S')
    book_request_date_formated.short_description = 'Book Request Date'
    
    def display_linked_client(self, obj):
        client = obj.user.client
        if client:
            client_url = reverse('admin:app_clients_client_change', args=[client.pk])
            return format_html('<a href="{}">{}</a>', client_url, client.company)
        return '-'
    display_linked_client.short_description = 'Client'
    
    def following_since_formated(self,obj):
        if not obj.following_since:
            return '-'
        return timezone.localtime(obj.following_since).strftime('%d-%m-%Y %H:%M:%S')
    following_since_formated.short_description = 'Following Since'
    
    def has_add_permission(self, request, obj):
        return False

class BookingInline(admin.TabularInline):
    model = Booking
    fields = ['display_linked_client','user', 'booking_amount_money', 'booking_date_formated','booking_date_expire', 'button_reactivate', 'reactivate_request_date_formated' ]
    readonly_fields = [ 'display_linked_client', 'user', 'booking_amount_money', 'booking_date_formated', 'booking_date_expire', 'button_reactivate', 'reactivate_request_date_formated']  
    # formset = BookingInlineFormSet
    extra = 0
    # if link required back to the booking 
    # dotn forget to remove the css then for hiding the title !
    # show_change_link = True
    can_delete = False
    # if collapsed functionality of bookings required
    # classes = ('collapse',)
    
    def display_linked_client(self, obj):
        client = obj.user.client
        if client:
            client_url = reverse('admin:app_clients_client_change', args=[client.pk])
            return format_html('<a href="{}">{}</a>', client_url, client.company)
        return '-'
    display_linked_client.short_description = 'Client'
    
    def button_reactivate(self, obj):
        booking_id = obj.id 
        url = reverse('app_funding:booking-reactivate-request',args=[booking_id])
        return format_html('<button type="button" class="reactivateButton" data-url="{}">Reactivate Request</button>', url)
    button_reactivate.short_description = 'Reactivate Request'
    
    def booking_date_formated(self, obj):
        return timezone.localtime(obj.booking_date).strftime('%d-%m-%Y %H:%M:%S')
    booking_date_formated.short_description = 'Booking Date'
    
    def booking_date_expire(self, obj):
        if not obj.booking_date_expire:
            return '-'
        return timezone.localtime(obj.booking_date_expire).strftime('%d-%m-%Y %H:%M:%S')
    booking_date_expire.short_description = 'Booking Date Expiration'
    
    def reactivate_request_date_formated(self, obj):
        if not obj.reactivate_request_date:
            return '-'
        return timezone.localtime(obj.reactivate_request_date).strftime('%d-%m-%Y %H:%M:%S')
    reactivate_request_date_formated.short_description = 'Reactivate Request Date'
    
    def has_add_permission(self, request, obj):
        return False

class ProjectAdmin(admin.ModelAdmin):
    # specify the fields to display in the admin list view
    list_display = ['name','online_from_formated','project_money_total','project_money_reached','project_money_rest','display_total_bookings', 'display_total_followers']
    # Make the name field clickable
    list_display_links = ('name',)
    # add a filter
    list_filter = ['name']
    # search field
    search_fields = ['name']
    # read only
    readonly_fields = ['online_from_formated','project_money_reached','project_money_rest', 'display_total_bookings','display_total_followers']
    
    # include extra css to hide the title of the inline element
    # marking with colors the projects taht are good to go
    class Media:
        css = {
            # for hiding the titel in the inline tabular
            # and ading red/green color highltigth to the project
            'all':('css/custom_admin.css',)
        }
        # adding collors to the projects that are good to go 
        # project_money_rest <= 0 , filed will be gree else field will be red
        js = ('js/custom_admin.js',)
    
    def display_total_followers(self,obj):
        return obj.get_all_followers
    display_total_followers.short_description = 'Total Followers'
    
    def display_total_bookings(self,obj):
        return obj.get_total_bookings
    display_total_bookings.short_description = 'Total Booking'
    
    def project_money_rest(self, obj):
        return obj.project_money_rest
    project_money_rest.short_description = 'Money Rest'
    
    def project_money_reached(self,obj):
        return obj.project_money_reached
    project_money_reached.short_description = 'Money Reached'
    
    def online_from_formated(self, obj):
        if not obj.online_from:
            return '-'
        return timezone.localtime(obj.online_from).strftime('%d-%m-%Y %H:%M:%S')
    online_from_formated.short_description = 'Online From'
    online_from_formated.admin_order_field = 'online_from'
    
    # specify the inlines
    inlines = [BookingInline,FollowerInline]
        
admin.site.register(Project,ProjectAdmin)


class BookingAdmin(admin.ModelAdmin): 
    list_display = ['booking_name','client','user','project', 'booking_amount_money','formated_booking_date', 'booking_date_expire','formated_reactivate_request_date']
    readonly_fields = ['booking_name','client','user','project', 'booking_amount_money','formated_booking_date', 'booking_date_expire', 'formated_reactivate_request_date']
    
    fields = ['display_linked_client','user','project', 'booking_amount_money','formated_booking_date', 'booking_date_expire','formated_reactivate_request_date']
    
    search_fields =['user__username', 'project__name']
    list_filter = ['booking_date', 'booking_amount_money'] 
    ordering = ['user', 'project','booking_date', 'booking_amount_money', 'reactivate_request_date'] 
    
    
    def booking_name(self,obj):
        return obj
    
    def client(self,obj):
        return obj.user.client
    
    def display_linked_client(self, obj):
        client = obj.user.client
        if client:
            client_url = reverse('admin:app_clients_client_change', args=[client.pk])
            return format_html('<a href="{}">{}</a>', client_url, client.company)
        return '-'
    display_linked_client.short_description = 'Client'
    
    def booking_date_expire(self, obj):
        return timezone.localtime(obj.booking_date_expire).strftime('%d-%m-%Y %H:%M:%S')
    booking_date_expire.short_description = 'Booking Date Expiration'

    
    def formated_booking_date(self, obj):
        return timezone.localtime(obj.booking_date).strftime('%d-%m-%Y %H:%M:%S')
    formated_booking_date.short_description = 'Booking Date'
    formated_booking_date.admin_order_field = 'booking_date'
    formated_booking_date.admin_filter_field = 'booking_date'
    
    
    def formated_reactivate_request_date(self, obj):
        if not obj.reactivate_request_date:
            return '-'
        return timezone.localtime(obj.reactivate_request_date).strftime('%d-%m-%Y %H:%M:%S')
    formated_reactivate_request_date.short_description = 'Reactivate request date'
    formated_reactivate_request_date.admin_order_field = 'reactivate_request_date'
    
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False
    
    def change_view(self, request, object_id, form_url='', extra_context=None):
        extra_context = extra_context or {}
        extra_context['show_save'] = False
        extra_context['show_save_and_continue'] = False
        return super().change_view(request, object_id, form_url, extra_context=extra_context)
    
    
admin.site.register(Booking, BookingAdmin)


class FollowerAdmin(admin.ModelAdmin):
    list_display = ['follower_name','client','user','project','following_since_formated']
    readonly_fields = ['follower_name', 'client','display_linked_client','user','project','following_since_formated']
    fields = ['display_linked_client','user','project','following_since_formated']
    ordering = ['following_since']
    search_fields =['user__username', 'project__name']
    show_change_link = True
    
    def follower_name(self,obj):
        return obj
    
    def client(self,obj):
        return obj.user.client
    
    def display_linked_client(self, obj):
        client = obj.user.client
        if client:
            client_url = reverse('admin:app_clients_client_change', args=[client.pk])
            return format_html('<a href="{}">{}</a>', client_url, client.company)
        return '-'
    display_linked_client.short_description = 'Client'
    
    
    def following_since_formated(self,obj):
        if not obj.following_since:
            return '-'
        return timezone.localtime(obj.following_since).strftime('%d-%m-%Y %H:%M:%S')
    following_since_formated.short_description = 'Following Since'
    following_since_formated.admin_order_field = 'following_since'
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False
    
admin.site.register(Follower, FollowerAdmin) 


class TokenAdmin(admin.ModelAdmin):
    list_display = ['token_name','booking','created_at_formated','expiration_date']
    readonly_fields = ['token_name','booking','token','created_at_formated','expiration_date']
    fields = ['booking','token','created_at_formated','expiration_date']
    
    def token_name(self,obj):
        return obj
    token_name.short_description = 'Token'
    
    def created_at_formated(self,obj):
        if not obj.created_at:
            return '-'
        return timezone.localtime(obj.created_at).strftime('%d-%m-%Y %H:%M:%S')
    created_at_formated.short_description = 'Created at'

    def expiration_date(self,obj):
        if not obj.expiration_date:
            return '-'
        return timezone.localtime(obj.expiration_date).strftime('%d-%m-%Y %H:%M:%S')
    expiration_date.short_description = 'Expiration Date'
        
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    def has_change_permission(self, request, obj=None) -> bool:
        return False
    
admin.site.register(Token, TokenAdmin) 
