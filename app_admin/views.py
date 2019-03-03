from django.shortcuts import render
from . import routers
import logging
from django.contrib.auth.decorators import login_required
from django.urls import reverse


logger = logging.getLogger(__name__)


@login_required(login_url='/login')
def index(request):
    p = routers.router()
    p['statistic']['active'] = 'active'
    print(p)
    return render(request, "index.html", p)
