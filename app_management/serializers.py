from rest_framework import serializers

from .models import AppUser, UserStatus, UserFriend

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = AppUser
        fields = ['id', 'username', 'avatar', 'email', 'is_active', 'sex', 'birth_year', 'bio', 'is_visible']


class UserStatusSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserStatus
        fields = '__all__'


class UserFriendSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserFriend
        fields = '__all__'
