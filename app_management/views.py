from rest_framework import viewsets

from .models import AppUser, UserFriend, UserStatus
from .serializers import UserFriendSerializer, UserStatusSerializer, UserSerializer

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = AppUser.objects.all()
    serializer_class = UserSerializer


class UserStatusViewSet(viewsets.ModelViewSet):
    queryset = UserStatus.objects.all()
    serializer_class = UserStatusSerializer


class UserFriendViewSet(viewsets.ModelViewSet):
    queryset = UserFriend.objects.all()
    serializer_class = UserFriendSerializer
