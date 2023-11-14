"""
Custom permissions for Article
"""
from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsOwnerOrReadOnly(BasePermission):
    """persmission to distinguish the users who are the owners
    of the object, only the owners can edit or delete it"""

    # the method checks if the user has the permissions to perform the
    # requested action on the object
    def has_object_permission(self, request, view, obj):
        """checks if the user has the permissions to perform requested action
        on the object"""
        if request.method in SAFE_METHODS:
            # returns True fro SAFE methods, such as ('GET', 'HEAD', 'OPTIONS')
            # only these methods will be allowed by default
            return True
        # other option is if the obj.author is the curenlty logedin user
        # checks if the object author matches the logged in user
        # so only the owner will have the write permissions
        return obj.author == request.user
