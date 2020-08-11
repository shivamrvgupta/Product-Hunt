from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'nick_name', 'mobile_no', 'modified_date')
    list_display_links = ('id', 'nick_name')
    list_per_page = 25


admin.site.register(UserProfile, UserAdmin)

# Register your models here.
