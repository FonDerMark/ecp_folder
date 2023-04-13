from django.http import JsonResponse, HttpResponse
from django.db import connection


def api_index(request):
    return JsonResponse(full_list(), safe=False)


def full_list(db_name='main_employees'):
    with connection.cursor() as cursor:
        cursor.execute(f'SELECT * FROM {db_name}')
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]
