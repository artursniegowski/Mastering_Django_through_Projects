"""
Views for the Profile model
"""
from django.contrib.auth import get_user_model

# from django.conf import settings
# settings.AUTH_USER_MODEL
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.exceptions import NotFound
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# TODO: change in porduction
from papyrus_portal_api.settings.local import DEFAULT_FROM_EMAIL
# from papyrus_portal_api.settings.production import DEFAULT_FROM_EMAIL

from .exceptions import CantFollowYourself
from .models import Profile
from .pagination import ProfilePagination
from .renderers import ProfileJSONRenderer, ProfilesJSONRenderer
from .serializers import FollowingSerializer, ProfileSerializer, UpdateProfileSerializer

User = get_user_model()


class ProfileListAPIView(ListAPIView):
    """get all the users porfiles"""

    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    pagination_class = ProfilePagination
    renderer_classes = [ProfilesJSONRenderer]


class ProfileDetailAPIView(RetrieveAPIView):
    """view for single user porfile"""

    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    renderer_classes = [ProfileJSONRenderer]

    def get_queryset(self):
        # retrives related data from other tables
        # django will autoamticaly retrive the related user objects
        # for each profile object in the same query
        queryset = Profile.objects.select_related("user")
        return queryset

    def get_object(self):
        # get user asociated wiwth the authenticated request
        user = self.request.user
        # finding the porfile tht is connected to this user and return it
        profile = self.get_queryset().get(user=user)
        return profile


class UpdateProfileAPIView(RetrieveAPIView):
    """view for updating profile"""

    serializer_class = UpdateProfileSerializer
    permission_classes = [IsAuthenticated]
    # multipart parser is used to parse multip-part or form data
    # so we are able to handle file uploads for the photo
    parser_classes = [MultiPartParser]
    renderer_classes = [ProfileJSONRenderer]

    def get_object(self):
        """retreiving the object"""
        return self.request.user.profile

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        # return super().patch(request, *args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


class FollowerListView(APIView):
    """Return a list of all the profiles that
    follow the user with the specified ID"""

    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        """retriving the user_id from teh URL"""
        try:
            profile = Profile.objects.get(user__id=request.user.id)
            follower_profiles = profile.followers.all()
            # it is  a mnay to many relationsip this is why we have many=True
            serializer = FollowingSerializer(follower_profiles, many=True)
            formatted_response = {
                "status_code": status.HTTP_200_OK,
                "followers_count": follower_profiles.count(),
                "followers": serializer.data,
            }
            return Response(formatted_response, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response(status=404)


class FollowingListView(APIView):
    """retrvices all the users a spacified user is following"""

    def get(self, request, user_id, format=None):
        # user_id is passed in get method as parameter
        try:
            profile = Profile.objects.get(user__id=user_id)
            following_profiles = profile.following.all()
            users = [p.user for p in following_profiles]
            serializer = FollowingSerializer(users, many=True)
            fortmatted_response = {
                "status_code": status.HTTP_200_OK,
                "following_count": following_profiles.count(),
                "users_i_follow": serializer.data,
            }
            return Response(fortmatted_response, status=status.HTTP_200_OK)
        except Profile.DoesNotExist:
            return Response(status=404)


class FollowAPIView(APIView):
    """Enables users to follow each other"""

    def post(self, request, user_id, format=None):
        """following the given user_id"""
        try:
            follower = Profile.objects.get(user=self.request.user)
            user_profile = request.user.profile
            profile = Profile.objects.get(user__id=user_id)
            # checks if the profile is the same as request to follow
            if profile == follower:
                raise CantFollowYourself()
            # checking if the user already follows that profile
            if user_profile.check_following(profile):
                formatted_response = {
                    "status_code": status.HTTP_400_BAD_REQUEST,
                    "message": f"You are already following {profile.user.first_name} {profile.user.last_name}",
                }
                return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

            user_profile.follow(profile)
            subject = "A new user follow you"
            message = f"Hi there, {profile.user.first_name}!!, the user {user_profile.user.first_name} {user_profile.user.last_name} now follows you"  # noqa
            from_email = DEFAULT_FROM_EMAIL
            recipient_list = [profile.user.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            return Response(
                {
                    "status_code": status.HTTP_200_OK,
                    "message": f"You are now following {profile.user.first_name} {profile.user.last_name}",
                }
            )
        except Profile.DoesNotExist:
            raise NotFound("You can't follow a profile that does not exists.")


class UnfollowAPIView(APIView):
    """view used to unfollow a porfile"""

    def post(self, request, user_id, *args, **kwargs):
        """unfollowing the given user_id"""
        user_profile = request.user.profile
        profile = Profile.objects.get(user__id=user_id)
        # checking if the porfile actally follows the given user_ids profile
        if not user_profile.check_following(profile):
            formatted_response = {
                "status_code": status.HTTP_400_BAD_REQUEST,
                "message": f"You can't unfollow {profile.user.first_name} {profile.user.last_name}, since you are not following this user in the first place.",  # noqa
            }
            return Response(formatted_response, status=status.HTTP_400_BAD_REQUEST)

        user_profile.unfollow(profile)
        formatted_response = {
            "status_code": status.HTTP_200_OK,
            "message": f"You have unfollow {profile.user.first_name} {profile.user.last_name}.",
        }
        return Response(formatted_response, status=status.HTTP_200_OK)
