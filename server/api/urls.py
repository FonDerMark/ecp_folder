from django.conf.urls import url
from .views import staff_list

urlpatterns = [
    url(r'^$', staff_list)
]