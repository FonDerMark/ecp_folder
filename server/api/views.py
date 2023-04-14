from django.http import JsonResponse, HttpResponse
from django.db import connection


def get_staff_list(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM main_employees me LEFT JOIN main_posts mp '
                       'on mp.id = me.post_id')
        columns = [col[0] for col in cursor.description]
        return JsonResponse([dict(zip(columns, row)) for row in cursor.fetchall()], safe=False)


def get_posts_list(request):
    with connection.cursor() as cursor:
        cursor.execute('SELECT * FROM main_posts')
        columns = [col[0] for col in cursor.description]
        return JsonResponse([dict(zip(columns, row)) for row in cursor.fetchall()], safe=False)

def get_employee_info(request):
    employee_id = request.GET.get('id')
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM main_employees me LEFT JOIN main_posts mp on mp.id = me.post_id WHERE me.id={employee_id}')
        columns = [col[0] for col in cursor.description]
        return JsonResponse([dict(zip(columns, row)) for row in cursor.fetchall()], safe=False)
