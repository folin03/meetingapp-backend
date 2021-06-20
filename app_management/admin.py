from django.contrib import admin

from .models import AppUser, UserFriend, UserStatus


admin.site.site_header = 'MeetingApp admin'
admin.site.site_title = 'MeetingApp admin'
admin.site.site_url = ''


admin.site.register(AppUser)
admin.site.register(UserStatus)
admin.site.register(UserFriend)