from django.http import JsonResponse, HttpResponse
from django.db import connection


def request_to_sql(sql_string) -> list:
    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        columns = [col[0] for col in cursor.description]
        return [dict(zip(columns, row)) for row in cursor.fetchall()]


def get_staff_list(request):
    sql_string = 'SELECT * FROM main_employees me LEFT JOIN main_posts mp on mp.id = me.post_id'
    return JsonResponse(request_to_sql(sql_string), safe=False)


def get_posts_list(request):
    sql_string = 'SELECT * FROM main_posts'
    return JsonResponse(request_to_sql(sql_string), safe=False)


def get_employee_info(request):
    employee_id = request.GET.get('id')
    sql_string = f'SELECT * FROM main_employees me LEFT JOIN main_posts mp on mp.id = me.post_id WHERE me.id={employee_id}'
    return JsonResponse(request_to_sql(sql_string)[0], safe=False)
