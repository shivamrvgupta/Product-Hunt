from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# # https://docs.djangoproject.com/en/3.1/topics/auth/customizing/#a-full-example


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nick_name = models.CharField(max_length=50)
    about = models.CharField(default=True, max_length=500)
    mobile_no = models.IntegerField(default=True)
    profile_pic = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    background_image = models.ImageField(
        upload_to='photos/%Y/%m/%d/', blank=True)
    created_date = models.DateTimeField(default=datetime.now, blank=True)
    modified_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.nick_name
