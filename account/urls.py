# -*- coding: utf-8 -*-
"""
 @Time    : 2019/3/3 16:12
 @Author  : CyanZoy
 @File    : urls.py
 @Software: PyCharm
 """
from django.conf.urls import url
from . import views

app_name = "account"

urlpatterns = [
    url(r'^login/$', views.LoginView.as_view(success_url='/'), name='login'),
    url(r'^qq_login/$', views.qq_login),
    # url(r'^register/$', views.RegisterView.as_view(success_url="/"), name='register'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout')
]