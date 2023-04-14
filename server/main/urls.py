from django.conf.urls import url

from . import views

#TODO test delete
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^test/$', views.test, name='test'),
]