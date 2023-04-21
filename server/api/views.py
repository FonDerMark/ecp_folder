from django.http import JsonResponse, HttpResponse
from django.db import connection
from django.shortcuts import redirect


def request_to_sql(sql_string) -> list:
    '''
    Функция принимает на вход строку запроса sql_string и параметр data_return,
    отвечающий за необходимость возвращения результата выполнения запроса.
    Функция выполняет запрос в БД и возвращает список словарей, содержащих результат запроса.
    Ключами словаря являются названия столбцов, а значениями - данные из ячеек таблицы,
    соответствующих этим столбцам.
    :param sql_string: Строка SQL запроса
    :return: list of dicts
    '''
    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        main_request = sql_string.split(' ')[0]
        if main_request == 'SELECT':
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]




# Все последующие функции являются простыми конструкторами строки SQL запроса



def get_staff_list(request):
    '''
    Функция для получения списка сотрудников
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
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
    return JsonResponse(request_to_sql(sql_string))


def get_employee_info(request):
    '''
    Функция для получения информации о сотруднике
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    if request.method == 'GET':
        employee_id = request.GET.get('id')
        sql_string = f'SELECT * FROM main_employees me ' \
                     f'LEFT JOIN main_posts mp on mp.id = me.post_id ' \
                     f'WHERE me.id={employee_id}'
    return JsonResponse(request_to_sql(sql_string)[0])


def add_new_employeer(request):
    '''
    Функция для добавления нового сотрудника
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    lastname = request.POST.get('lastname')
    firstname = request.POST.get('firstname')
    surname = request.POST.get('surname')
    post_id = request.POST.get('post_id')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    sql_string = f"INSERT INTO main_employees (lastname, firstname, surname, post_id, age, gender) " \
                 f"VALUES ('{lastname}', '{firstname}', '{surname}', '{post_id}', '{age}', '{gender}')"
    request_to_sql(sql_string)
    return redirect('employeers_list')


def edit_employeer(request):
    '''
    Функция для редактирования данных сотрудника
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    qd = {k: v[0] for k, v in dict(request.POST).items()}
    del qd['csrfmiddlewaretoken']
    me_id = int(qd.pop('id'))
    params = [k + '=' + '\'' + v + '\'' for k, v in qd.items()]
    sql_string = f"UPDATE main_employees SET {', '.join(params)} WHERE id={me_id}"
    request_to_sql(sql_string)
    return redirect('employeers_list')


def employeer_delete(request):
    '''
    Функция для удаления сотрудника
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    deleted_id = request.GET['id']
    sql_string = f"DELETE FROM main_employees WHERE id={deleted_id}"
    request_to_sql(sql_string)
    return redirect('employeers_list')


def get_posts_list(request):
    '''
    Функция для добавления нового сотрудника
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    sql_string = 'SELECT * FROM main_posts'
    return JsonResponse(request_to_sql(sql_string))


def add_new_post(request):
    '''
    Функция для добавления новой должности
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    post_name = request.POST.get('post')
    cat_name = request.POST.get('category')
    sql_string = f"INSERT INTO main_posts (post, category) VALUES ('{post_name}', '{cat_name}')"
    request_to_sql(sql_string)
    return redirect('posts_list')


def get_post_info(request):
    '''
    Функция для получения информации о должности
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    post_id = request.GET.get('post_id')
    sql_string = f'SELECT * FROM main_posts WHERE id={post_id}'
    return JsonResponse(request_to_sql(sql_string)[0])


def post_edit(request):
    '''
    Функция для редактирования должности
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    print(request.POST)
    post_id = request.POST.get('post_id')
    post = request.POST.get('post')
    category = request.POST.get('category')
    sql_string = f"UPDATE main_posts SET post='{post}', category='{category}' WHERE id={post_id}"
    request_to_sql(sql_string)
    return redirect('posts_list')


def post_delete(request):
    '''
    Функция для удаления должности
    :param request: HttpRequest объект, который содержит информацию о запросе
    :return: JSON
    '''
    deleted_id = request.GET['id']
    sql_string = f"DELETE FROM main_posts WHERE id={deleted_id}"
    print(sql_string)
    request_to_sql(sql_string)
    return redirect('posts_list')
