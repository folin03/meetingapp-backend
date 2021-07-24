from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view

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


@api_view(['GET'])
def verify_user_token(request):
    """
    verify user exists (used for login)
    """
    if request.method == 'GET':
        user = AppUser.objects.get(id=request.user.id)
        serializer = UserSerializer(user, context={'request': request}, many=False)
        return Response(serializer.data)
