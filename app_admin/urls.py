# -*- coding: utf-8 -*-
from django.conf import urls
from django.urls import path
from . import views
from django.conf.urls import url
"""
 @Time    : 2019/3/2 16:48
 @Author  : CyanZoy
 @File    : urls.py
 @Software: PyCharm
 """
urlpatterns = [
    path("", views.index),
    path("index", views.index),
    url('^publish/$', views.publish),
    url('article/save', views.save_article),
    path('article/update/<str:uuid>', views.update_article),
    url('author/info', views.author),
    url('author/author_info_update', views.author_update),
    path('manage/<int:page>', views.manage),
    url('^manage/$', views.manage),
    path('manage/edit/markdown/<str:uuid>', views.manage_markdown),
    path('manage/edit/<str:uuid>', views.manage_edit),
    url('image/upload', views.img)
]
