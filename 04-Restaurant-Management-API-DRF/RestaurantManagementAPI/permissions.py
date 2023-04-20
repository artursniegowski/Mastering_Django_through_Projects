from rest_framework.permissions import BasePermission


class ManagersOnlyPermission(BasePermission):
    """persmission to distinguish only users who are in the managers group"""
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Manager').exists(): 
            return True
        return False
 
class DeliveryCrewOnlyPermission(BasePermission):
    """persmission to distinguish only users who are in the delivery crew"""
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Delivery_Crew').exists():
            return True
        return False

class CustomersOnlyPermission(BasePermission):
    """persmission to distinguish only users who are customers, so they are not in delivery crew nor in the mangers crew"""
    def has_permission(self, request, view):
        if not request.user.groups.filter(name='Manager').exists() and not request.user.groups.filter(name='Delivery_Crew').exists():
            return True
        return False
    
