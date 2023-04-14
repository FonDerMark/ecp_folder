from django.http import JsonResponse, HttpResponse
from django.db import connection


def staff_list(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM main_employees me LEFT JOIN main_posts mp on mp.id = me.post_id')
        columns = [col[0] for col in cursor.description]
        return JsonResponse([dict(zip(columns, row)) for row in cursor.fetchall()], safe=False)


def posts_list(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM main_posts')
        columns = [col[0] for col in cursor.description]
        return JsonResponse([dict(zip(columns, row)) for row in cursor.fetchall()], safe=False)


def full_list(table_name) -> list:
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM {table_name}')
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
