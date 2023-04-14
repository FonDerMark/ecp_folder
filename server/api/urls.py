from django.conf.urls import url
from .views import get_staff_list

urlpatterns = [
    url(r'^$', get_staff_list)
]