from django.conf.urls import url, include
from main.models import Employees, Posts
from rest_framework import serializers, viewsets, routers


class EmployeesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"


class PostsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Posts
        fields = "__all__"


# ViewSets define the view behavior.
class EmployeesViewSet(viewsets.ModelViewSet):
    queryset = Employees.objects.all()
    serializer_class = EmployeesSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer


router = routers.DefaultRouter()
router.register(r'employees', EmployeesViewSet)
router.register(r'posts', PostsViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
