from django.shortcuts import render
from .models import Employees, Posts


def index(request):
    context = {
        'employees': Employees.objects.raw('SELECT * FROM main_employees'),
        'posts': Posts.objects.raw('SELECT * FROM main_posts'),
    }
    return render(request, 'index.html', context)
