from rest_framework import serializers

from .models import AppUser, UserStatus, UserFriend

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = '__all__'


class UserStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserStatus
        fields = '__all__'


class UserFriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserFriend
        fields = '__all__'
