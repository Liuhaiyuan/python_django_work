from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.blog_app_title, name='blog_app_title'),
    url(r'(?P<article_id>\d)/$', views.blog_app_article, name='blog_app_detail')
]