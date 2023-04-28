import sqlite3

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
            [cursor.execute(request) for request in list_of_requests]
            cursor.execute('COMMIT')
            print(cursor.statusmessage)
    except:
        cursor.execute('ROLLBACK')
        print(cursor.statusmessage)


def database_preparation():
    config = request_to_sql('SELECT * FROM main_config')
    try:
        salary_fund = "INSERT INTO main_config (name, value_int) VALUES ('salary_fund', 1000000000)"
        request_to_sql(salary_fund)
    except:
        print('Salary fund exist')
    try:
        request_str = 'CREATE VIEW emp_balanse AS ' \
                      'SELECT me.lastname, me.firstname me.surname mb.account_balance ' \
                      'FROM main_employees me ' \
                      'LEFT JOIN main_accountbalance mb ON me.id = mb.employee_id'
        print(request_str)
        with connection.cursor() as cursor:
            cursor.execute(request_str)
    except:
        pass