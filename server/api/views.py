from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.shortcuts import redirect


def request_to_sql(sql_string, data_return=True) -> list:
    '''
    Коннектор для передачи строки с запросом напрямую в БД, и
    получения ответа, с последующим оформлением результата двумя генераторами.
    Все последующие функции благодаря такому подходу, фактически
    являются простыми конструкторами строки запроса.
    Параметр data_return отвечает за правильную работу функции, при использовании в конструкциях,
    где отсутствует возвращаемое значение, параметру необходимо выставить значение False.
    '''
    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        if data_return:
            try:
                columns = [col[0] for col in cursor.description]
            finally:
                return [dict(zip(columns, row)) for row in cursor.fetchall()]






def get_staff_list(request):
    sql_string = 'SELECT ' \
                 'me.id, ' \
                 'me.lastname, ' \
                 'me.firstname, ' \
                 'me.surname, ' \
                 'me.post_id, ' \
                 'me.gender, ' \
                 'me.age, ' \
                 'mp.id as post_id, ' \
                 'mp.post, ' \
                 'mp.category ' \
                 'FROM main_employees me ' \
                 'LEFT JOIN main_posts mp on me.post_id = mp.id ' \
                 'ORDER BY me.lastname, me.firstname'
    return JsonResponse(request_to_sql(sql_string), safe=False)


def get_employee_info(request):
    if request.method == 'GET':
        employee_id = request.GET.get('id')
        sql_string = f'SELECT * FROM main_employees me ' \
                     f'LEFT JOIN main_posts mp on mp.id = me.post_id ' \
                     f'WHERE me.id={employee_id}'
    return JsonResponse(request_to_sql(sql_string)[0], safe=False)


def add_new_employeer(request):
    lastname = request.POST.get('lastname')
    firstname = request.POST.get('firstname')
    surname = request.POST.get('surname')
    post_id = request.POST.get('post_id')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    sql_string = f"INSERT INTO main_employees (lastname, firstname, surname, post_id, age, gender) " \
                 f"VALUES ('{lastname}', '{firstname}', '{surname}', '{post_id}', '{age}', '{gender}')"
    request_to_sql(sql_string, data_return=False)
    return redirect('employeers_list')


def edit_employeer(request):
    qd = {k: v[0] for k, v in dict(request.POST).items()}
    del qd['csrfmiddlewaretoken']
    me_id = int(qd.pop('id'))
    params = [k + '=' + '"' + v + '"' for k, v in qd.items()]
    sql_string = f"UPDATE main_employees SET {', '.join(params)} WHERE id={me_id}"
    request_to_sql(sql_string, data_return=False)
    return redirect('employeers_list')


def employeer_delete(request):
    deleted_id = request.GET['id']
    sql_string = f"DELETE FROM main_employees WHERE id={deleted_id}"
    print(sql_string)
    request_to_sql(sql_string, data_return=False)
    return redirect('employeers_list')


def get_posts_list(request):
    sql_string = 'SELECT * FROM main_posts'
    return JsonResponse(request_to_sql(sql_string), safe=False)


def add_new_post(request):
    post_name = request.POST.get('post')
    cat_name = request.POST.get('category')
    sql_string = f"INSERT INTO main_posts (post, category) VALUES ('{post_name}', '{cat_name}')"
    request_to_sql(sql_string, data_return=False)
    return redirect('posts_list')


def get_post_info(request):
    post_id = request.GET.get('post_id')
    sql_string = f'SELECT * FROM main_posts WHERE id={post_id}'
    return JsonResponse(request_to_sql(sql_string)[0], safe=False)


def post_edit(request):
    print(request.POST)
    post_id = request.POST.get('post_id')
    post = request.POST.get('post')
    category = request.POST.get('category')
    sql_string = f"UPDATE main_posts SET post='{post}', category='{category}' WHERE id={post_id}"
    request_to_sql(sql_string, data_return=False)
    return redirect('posts_list')


def post_delete(request):
    deleted_id = request.GET['id']
    sql_string = f"DELETE FROM main_posts WHERE id={deleted_id}"
    print(sql_string)
    request_to_sql(sql_string, data_return=False)
    return redirect('posts_list')
