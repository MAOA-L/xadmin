from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import now


class BlogUser(AbstractUser, models.Model):
    id = models.AutoField("ID", primary_key=True)
    openId = models.CharField(max_length=50)
    gmtCreate = models.DateTimeField("创建时间", default=now)
    gmtModified = models.DateTimeField("修改时间", default=now)
    phoneNumber = models.CharField("手机号", max_length=20)
    nickname = models.CharField('昵称', max_length=100, blank=True)
    mugshot = models.ImageField('头像', upload_to='upload/mugshots', blank=True)
    motto = models.CharField('座右铭', max_length=255, null=True)

