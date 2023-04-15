from django.conf.urls import url
from .views import get_staff_list, get_posts_list, get_employee_info, edit_employeer

urlpatterns = [
    url(r'^staff/$', get_staff_list, name='get_staff_list'),
    url(r'^posts/$', get_posts_list, name='get_posts_list'),
    url(r'^lcard/$', get_employee_info, name='get_one_card'),
    url(r'^employeer_edit/$', edit_employeer, name='employeer_edit'),
]