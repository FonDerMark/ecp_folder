from django.test import TestCase
from .models import Employees, Posts

emps = Employees.objects.raw('SELECT * FROM main_employees')