from django.shortcuts import render
from .models import Employees, Posts


def index(request):
    return render(request, 'index.html')


# TODO Delete whis
def test(request):
    return render(request, 'base_page.html')
