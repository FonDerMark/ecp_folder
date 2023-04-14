from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^card_edit/$', views.card_edit, name='card_edit'),
]
