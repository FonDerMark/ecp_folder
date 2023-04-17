from django.conf.urls import url
from .views import get_staff_list, get_employee_info, edit_employeer, add_new_employeer, employeer_delete
from .views import get_posts_list, post_edit, add_new_post, get_post_info, post_delete

urlpatterns = [
    url(r'^staff/$', get_staff_list, name='get_staff_list_api'),
    url(r'^employeer_get/', get_employee_info, name='get_one_card_api'),
    url(r'^employeer_edit/$', edit_employeer, name='employeer_edit_api'),
    url(r'^employeer_add/$', add_new_employeer, name='employeer_add_api'),
    url(r'^employeer_delete/$', employeer_delete, name='employeer_add_api'),
    url(r'^posts/$', get_posts_list, name='get_posts_list_api'),
    url(r'^post_edit/$', post_edit, name='post_edit_api'),
    url(r'^post_get/$', get_post_info, name='post_get_api'),
    url(r'^post_add/$', add_new_post, name='post_add_api'),
    url(r'^post_delete/$', post_delete, name='post_delete_api'),
]