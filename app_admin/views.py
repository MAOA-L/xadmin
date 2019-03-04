from django.shortcuts import render
from . import routers
import logging
from django.contrib.auth.decorators import login_required


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
