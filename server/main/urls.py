from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='employeers_list'),
    url(r'^card_edit/$', views.card_edit, name='card_edit'),
    url(r'^posts_list/$', views.list_posts, name='posts_list'),
]
