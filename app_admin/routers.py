# -*- coding: utf-8 -*-
"""
 @Time    : 2019/3/2 21:53
 @Author  : CyanZoy
 @File    : routers.py
 @Software: PyCharm
 """


def router(*args):
    return {
        'statistic': {
            'url': '/index',
            'name': '统计'
        },
        'article': {
            'publish': {
                'url': '/publish',
                'name': '文章发表',
                'active': ''
            },
            'manager': {

            },
            'active': '',
        },
        'author': {
            'info': {
                'url': '/author/info',
                'name': '信息',
                'active': ''
            },

            'active': '',
        }
    }
