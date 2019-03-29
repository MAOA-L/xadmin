from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, HttpResponse

from account.models import BlogUser
from . import routers
import logging
from django.contrib.auth.decorators import login_required, permission_required
import uuid
from .models import Sort, Images
import json, re
from django.contrib import auth
from .models import Article

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
    logger.info("in")
    if request.is_ajax():
        article = Article(
            uuid=uuid.uuid1(),
            sort=request.POST.get('sort_name'),
            markdown=request.POST.get('markdown'),
            text=request.POST.get('article'),
            label=request.POST.get('label_name'),
            title=request.POST.get('title_name'),
        )
        article.save()

    return HttpResponse(json.dumps({"code": 200, "msg": "保存成功"}))


@permission_required('change_article')
def update_article(request, uuid):
    logger.info("in")
    if request.is_ajax():
        article = Article.objects.get(uuid=uuid)
        article.markdown = request.POST.get('markdown')
        article.text = request.POST.get('article')
        article.save()

        return HttpResponse(json.dumps({"code": 200, "msg": "更新成功"}))
    else:
        return HttpResponse(json.dumps({"code": 30002, "msg": "更新失败"}))


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


def manage(request, page=1):
    print(page)
    article_list = Article.objects.all().order_by('-gmt_create')
    paginator = Paginator(article_list, 15)
    try:
        p = paginator.page(page)
    except PageNotAnInteger:
        p = paginator.page(1)
    except EmptyPage:
        p = paginator.page(paginator.num_pages)

    g = routers.router()
    g['article']['active'] = g['article']['manage']['active'] = 'active'
    g['article_list'] = p
    return render(request, "manage.html", g)


def manage_edit(request, uuid=None):
    if uuid and uuid is not '':
        return render(request, "edit.html", {"uuid": uuid})
    else:
        return HttpResponse({"code": 33002, "msg": "不存在的文章"})


def manage_markdown(request, uuid=None):
    if uuid and uuid is not '':
        return HttpResponse(Article.objects.get(uuid=uuid).markdown)
    else:
        return HttpResponse({"code": 33002, "msg": "不存在的文章"})

