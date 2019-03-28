from django.shortcuts import render, HttpResponse

from account.models import BlogUser
from . import routers
import logging
from django.contrib.auth.decorators import login_required, permission_required
import uuid
from .models import Sort, Images
import json, re
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

    return HttpResponse(json.dumps({"code": 200, "msg": "保存成功"}))


@login_required()
def author(request):
    p = routers.router()
    p['author']['active'] = p['author']['info']['active'] = 'active'
    p['user'] = request.user
    return render(request, "author_info.html", p)


def author_update(request):
    u = request.user
    u.username = request.POST.get("username")
    u.first_name = request.POST.get("first_name")
    u.last_name = request.POST.get("last_name")
    u.email = request.POST.get("email")
    u.phoneNumber = request.POST.get("phoneNumber")
    u.motto = request.POST.get("motto")
    BlogUser.save(u)
    return HttpResponse(json.dumps({"code": 200}))


def img(request):
    uid = uuid.uuid1()
    name = "http://"+request.get_host()+"/media/"
    print(name)
    if request.method == 'POST':
        new_img = Images(
            uuid=uid,
            img=request.FILES.get('file'),
            name=name
        )
        new_img.save()
    ni = Images.objects.get(uuid=uid)
    return HttpResponse(json.dumps({"code": 200, "data": ni.name+str(ni.img)}))
