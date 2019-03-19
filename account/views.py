from django.contrib import auth
from django.contrib.auth import REDIRECT_FIELD_NAME, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponseRedirect
# from django.contrib.sites.models import Site
from django.urls import reverse
from django.utils.decorators import method_decorator
from django.utils.http import is_safe_url
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView

from account.forms import LoginForm
from . models import BlogUser
import requests
import re
import json
from django.core.cache import cache

SESSION_KEY = '_auth_user_openid'


class LogoutView(RedirectView):
    url = '/login/'

    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):
        return super(LogoutView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # from DjangoBlog.utils import cache
        # cache.clear()
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'login.html'
    success_url = '/'
    redirect_field_name = REDIRECT_FIELD_NAME

    @method_decorator(sensitive_post_parameters('password'))
    @method_decorator(csrf_protect)
    @method_decorator(never_cache)
    def dispatch(self, request, *args, **kwargs):

        return super(LoginView, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        redirect_to = self.request.GET.get(self.redirect_field_name)
        if redirect_to is None:
            redirect_to = '/'
        kwargs['redirect_to'] = redirect_to

        return super(LoginView, self).get_context_data(**kwargs)

    def form_valid(self, form):
        form = AuthenticationForm(data=self.request.POST, request=self.request)
        print(form)
        if form.is_valid():
            # from DjangoBlog.utils import cache
            # if cache and cache is not None:
            #     cache.clear()
            print(self.redirect_field_name)
            redirect_to = self.request.GET.get(self.redirect_field_name)
            auth.login(self.request, form.get_user())
            return super(LoginView, self).form_valid(form)
            # return HttpResponseRedirect('/')
        else:
            return self.render_to_response({
                'form': form
            })

    def get_success_url(self):

        redirect_to = self.request.POST.get(self.redirect_field_name)
        if not is_safe_url(url=redirect_to, allowed_hosts=[self.request.get_host()]):
            redirect_to = self.success_url
        return redirect_to


def qq_login(request):

    print("in")
    # 根据参数返回需要获取code的url
    # 根据回调过来的code获取access_token
    client_id = 101549521
    client_secret = "df357795e13de29dcd168354b34f0509"
    code = request.GET.get("code")
    redirect_uri = "http://mfweb.cyanzoy.top:8080/xadmin/qq_login"
    url = "https://graph.qq.com/oauth2.0/token?grant_type=authorization_code&client_id={}&client_secret={}&code={}&redirect_uri={}"
    p = requests.get(url=url.format(client_id, client_secret, code, redirect_uri)).content.decode("UTF-8")
    # 输出access_token等信息
    list_three = p.split("&")
    print(p)
    three_arg = {}
    for _ in list_three:
        three_arg[_.split("=")[0]] = _.split("=")[1]

    # 根据access_token获取openid
    clientid_openid = requests.get(url="https://graph.qq.com/oauth2.0/me?access_token={}".format(three_arg["access_token"])).content.decode("UTF-8")
    callback = re.match("callback\((.*)\)", clientid_openid).group(1)
    callback_json = json.loads(callback)
    openid = callback_json["openid"]
    print('openid', openid)
    # 若数据库中已经保存openId则终止
    qquser = BlogUser.objects.get(openId=openid)
    if qquser:
        auth.login(request, qquser)
        # request.session[SESSION_KEY] = qquser.username
    if request.user.is_authenticated:
        print("已经认证")
    else:
        print("ai")
    # 若数据库中无此openId则将之后将用户信息保存至数据库
    # Access Token以及OpenID来访问用户信息->openid来识别用户
    user = requests.get("https://graph.qq.com/user/get_user_info?access_token={}&oauth_consumer_key={}&openid={}"
                        .format(three_arg["access_token"], client_id, openid)).content.decode("utf-8")

    # return render(request, "index.html", {"user": json.loads(user)})
    return HttpResponseRedirect("/index")
