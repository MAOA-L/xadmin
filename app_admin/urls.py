# -*- coding: utf-8 -*-
from django.conf import urls
from django.urls import path
from . import views
"""
 @Time    : 2019/3/2 16:48
 @Author  : CyanZoy
 @File    : urls.py
 @Software: PyCharm
 """
urlpatterns = [
    path("", views.index),
    path("index", views.index),
    # path("login", views.login),

]