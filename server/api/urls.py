from django.conf.urls import url
from .views import get_staff_list, get_posts_list, get_employee_info

urlpatterns = [
    url(r'^$', get_staff_list, name='get_stall_list'),
    url(r'^lcard/$', get_employee_info, name='get_one_card'),
]