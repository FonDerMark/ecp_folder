from django.http import JsonResponse, HttpResponse
from django.db import connection


def api_index(request):
    db_connect()
    return HttpResponse('Hello')


def db_connect():
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM main_employees')
        row = cursor
        print(result)
