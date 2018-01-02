from django.conf.urls import url
from . import views
from django.conf import settings

from django.contrib.auth import views as auth_views

urlpatterns = [
    # url(r'^login/$', views.user_login, name='user_login')   # 自定义的登录
    url(r'login/$', auth_views.login, name='user_login')      # django内置的登录
]