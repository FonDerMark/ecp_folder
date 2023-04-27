from django.db import connection


def request_to_sql(sql_string) -> list:
    '''
    Функция принимает на вход строку запроса sql_string.
    Функция выполняет запрос в БД и, при необходимости,
    возвращает список словарей, содержащих результат запроса.
    Ключами словаря являются названия столбцов, а значениями -
    данные из ячеек таблицы, соответствующих этим столбцам.
    :param sql_string: Строка SQL запроса
    :return: list of dicts
    '''
    with connection.cursor() as cursor:
        cursor.execute(sql_string)
        main_request = sql_string.split(' ')[0]
        if main_request == 'SELECT':
            columns = [col[0] for col in cursor.description]
            return [dict(zip(columns, row)) for row in cursor.fetchall()]


def transaction(list_of_requests):
    try:
        with connection.cursor as cursor:
            cursor.execute('BEGIN')
            [cursor.execute(i) for i in list_of_requests]
            cursor.execute('COMMIT')
            print(cursor.statusmessage)
    except:
        cursor.execute('ROLLBACK')
        print(cursor.statusmessage)
