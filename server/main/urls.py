from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^employeers_list/', views.employeers_list, name='employeers_list'),
    url(r'^employeer_edit/', views.employeer_edit, name='employeer_edit'),
    url(r'^employeer_add/', views.employeer_add, name='employeer_add'),
    url(r'^posts_list/', views.posts_list, name='posts_list'),
    url(r'^posts_edit/', views.posts_list, name='posts_edit'),
    url(r'^posts_add/', views.posts_list, name='posts_add'),
]