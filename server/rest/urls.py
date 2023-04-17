from django.conf.urls import url, include
from rest_framework import routers

from rest import views

router = routers.DefaultRouter()
router.register(r'employees', views.EmployeesViewSet)
router.register(r'posts', views.PostsViewSet)

urlpatterns = [
    url('^', include(router.urls)),
    url('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

urlpatterns += router.urls