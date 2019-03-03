# -*- coding: utf-8 -*-
"""
 @Time    : 2019/3/3 19:40
 @Author  : CyanZoy
 @File    : form.py
 @Software: PyCharm
 """
from django.contrib.auth.forms import AuthenticationForm
from django.forms import widgets


class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget = widgets.TextInput(attrs={'placeholder': "username", "class": "form-control"})
        self.fields['password'].widget = widgets.PasswordInput(attrs={'placeholder': "password", "class": "form-control"})
