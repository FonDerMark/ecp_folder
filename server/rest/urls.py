from django.conf.urls import url, include
from main.models import Employees, Posts
from rest_framework import serializers, viewsets, routers


# Сериализаторы определяют представление API.
class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


# Наборы представлений определяют поведение представления.
class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)
router.register(r'posts', PostsViewSet)

# подключение API, используя автоматическую маршрутизацию URL.
urlpatterns = [
    url(r'^', include(router.urls)),
]
