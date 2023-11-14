"""
Views for the user API
"""
from django.contrib.auth import get_user_model
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class CustomUserDetailsView(RetrieveUpdateAPIView):
    """Manage authenticated user"""

    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        """Retrives and returns the authenticated user"""
        # the user has to be authenticated based on the classes
        # that we set above
        return self.request.user

    def get_queryset(self):
        """returns an empty queryset"""
        # returns an empty queryset, to prevent any actual queryset from being
        # executed on the database from this view
        return get_user_model().objects.none()
