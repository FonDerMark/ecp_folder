from main.models import Employees, Posts
from rest_framework import permissions, viewsets

from .serializers import EmployeersSerializer, PostsSerializer


class EmployeesViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows employees to be viewed or edited.
    """
    queryset = Employees.objects.all().order_by('lastname', 'firstname')
    serializer_class = EmployeersSerializer


class PostsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Posts.objects.all()
    serializer_class = PostsSerializer