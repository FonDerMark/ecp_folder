from django.conf.urls import url
from .views import api_index

urlpatterns = [
    url(r'^$', api_index)
]