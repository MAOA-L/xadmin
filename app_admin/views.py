from django.shortcuts import render, HttpResponse
from . import routers
import logging
from django.contrib.auth.decorators import login_required, permission_required
import uuid
from .models import Sort
import json
from django.contrib import auth

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

SESSION_KEY = '_auth_user_openid'


@login_required(login_url='/login')
def index(request):
    user = request.user
    print(user)
    logger.info("view->index")
    p = routers.router()
    p['statistic']['active'] = 'active'
    p['user'] = user
    return render(request, "index.html", p)


@login_required()
def publish(request):
    logger.info("view->publish")
    # 激活菜单
    p = routers.router()
    p['article']['active'] = p['article']['publish']['active'] = 'active'
    # 获取分类
    sort = Sort.objects.all()
    p['sort'] = sort
    return render(request, "publish.html", p)


def set_active():
    pass


@permission_required('add_article')
def save_article(request) -> "save article":
    from .models import Article
    logger.info("in")
    if request.is_ajax():
        article = Article()
        sort_name = request.POST.get('sort_name')
        text = request.POST.get('article')
        label_name = request.POST.get('label_name')
        title_name = request.POST.get('title_name')

        article.uuid = uuid.uuid1()
        article.title = title_name
        article.sort = sort_name
        article.label = label_name
        article.text = text
        article.save()
        print(sort_name, article, label_name, title_name)

    return HttpResponse("emmm")


def author(request):
    p = routers.router()
    p['author']['active'] = p['author']['info']['active'] = 'active'
    return render(request, "author_info.html", p)


def author_update(request):
    print(request.POST.get("username"))
    return HttpResponse("e")
