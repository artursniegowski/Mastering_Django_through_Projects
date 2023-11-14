"""
Views for the Responses model
"""
from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404,
)
from rest_framework.permissions import IsAuthenticated

from .models import Article, Response
from .serializers import ResponseSerializer


class ResponseListCreateView(ListCreateAPIView):
    """Resonse create and list view"""

    queryset = Response.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ResponseSerializer

    def get_queryset(self):
        article_id = self.kwargs.get("article_id")
        return Response.objects.filter(article__id=article_id, parent_response=None)

    def perform_create(self, serializer):
        user = self.request.user
        article_id = self.kwargs.get("article_id")
        article = get_object_or_404(Article, id=article_id)
        serializer.save(user=user, article=article)


class ResponseUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    """Resonse update - delete - retrive view"""

    queryset = Response.objects.all()
    serializer_class = ResponseSerializer
    lookup_field = "id"

    def perform_update(self, serializer):
        """checking it the user owns the response - only the
        owner can edit the resposne"""
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied("You do not have permission to edit this response.")
        serializer.save()

    def perform_destroy(self, instance):
        """making sure only the owner of the repsonse can delete it"""
        user = self.request.user
        response = self.get_object()
        if user != response.user:
            raise PermissionDenied(
                "You do not have permission to delete this response."
            )
        instance.delete()
