from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.shortcuts import redirect


def request_to_sql(sql_string) -> list:
    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        try:
            columns = [col[0] for col in cursor.description]
        finally:
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


def get_staff_list(request):
    sql_string = 'SELECT * FROM main_employees me LEFT JOIN main_posts mp on mp.id = me.post_id'
    return JsonResponse(request_to_sql(sql_string), safe=False)


def get_posts_list(request):
    sql_string = 'SELECT * FROM main_posts'
    return JsonResponse(request_to_sql(sql_string), safe=False)


def get_employee_info(request):
    if request.method == 'GET':
        employee_id = request.GET.get('id')
        sql_string = f'SELECT * FROM main_employees me ' \
                     f'LEFT JOIN main_posts mp on mp.id = me.post_id ' \
                     f'WHERE me.id={employee_id}'
    return JsonResponse(request_to_sql(sql_string)[0], safe=False)


def get_post_info(request):
    post_id = request.GET.get('id')
    sql_string = f'SELECT * FROM main.main_posts WHERE id={post_id}'
    return JsonResponse(request_to_sql(sql_string)[0], safe=False)


def add_new_employeer(request):
    lastname = request.POST.get('lastname')
    firstname = request.POST.get('firstname')
    surname = request.POST.get('surname')
    post_id = request.POST.get('post_id')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    sql_string = f'INSERT INTO main.main_employees (lastname, firstname, surname, post_id, age, gender)' \
                 f'VALUES ({lastname}, {firstname}, {surname}, {post_id}, {age}, {gender})'
    return JsonResponse(request_to_sql(sql_string)[0], safe=False)


def edit_employeer(request):
    qd = {k: v[0] for k, v in dict(request.POST).items()}
    del qd['csrfmiddlewaretoken']
    #TODO post
    del qd['post']
    me_id = int(qd.pop('id'))
    params = [k + '=' + '"' + v + '"' for k, v in qd.items()]
    sql_string = f"UPDATE main_employees SET {', '.join(params)} WHERE id={me_id}"
    print(sql_string)
    request_to_sql(sql_string)
    return redirect('employeers_list')


def add_new_post(request):
    post_name = request.POST.get('post_name')
    cat_name = request.POST.get('cat_name')
    sql_string = f'INSERT INTO main.main_posts (post, category)' \
                 f'VALUES ({post_name}, {cat_name})'
    return JsonResponse(request_to_sql(sql_string)[0], safe=False)
