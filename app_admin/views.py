from django.shortcuts import render, HttpResponse
from . import routers
import logging
from django.contrib.auth.decorators import login_required, permission_required
import uuid

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


@login_required(login_url='/login')
def index(request):
    logger.info("view->index")
    p = routers.router()
    p['statistic']['active'] = 'active'
    return render(request, "index.html", p)


@login_required()
def publish(request):
    logger.info("view->publish")
    p = routers.router()
    p['article']['active'] = p['article']['publish']['active'] = 'active'
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

