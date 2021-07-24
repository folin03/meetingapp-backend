from rest_framework import routers

from app_management import views


# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'user-friends', views.UserFriendViewSet)
router.register(r'user-statuses', views.UserStatusViewSet)
