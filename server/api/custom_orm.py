from django.db import connection


class MyORM:

    def request_to_sql(self) -> list:
        with connection.cursor() as cursor:
            cursor.execute(self)
            main_request = self.split(' ')[0]
            if main_request == 'SELECT':
                columns = [col[0] for col in cursor.description]
                return [dict(zip(columns, row)) for row in cursor.fetchall()]

    def orm_delete(self, table_name, deleted_id):
        sql_str = f'DELETE FROM {table_name} WHERE id={deleted_id}'
        self.request_to_sql(sql_str)

    def orm_insert(self, table_name, fields, values):
        fields_str = ', '.join(fields)
        values_str = ', '.join(['\'' + i + '\'' for i in values])
        sql_str = f'INSERT INTO {table_name} ({fields}) VALUES '

    # def orm_update(self, table_name):
    #     qd = {k: v[0] for k, v in dict(request.POST).items()}
    #     del qd['csrfmiddlewaretoken']
    #     me_id = int(qd.pop('id'))
    #     params = [k + '=' + '\'' + v + '\'' for k, v in qd.items()]
    #     sql_string = f"UPDATE main_employees SET {', '.join(params)} WHERE id={me_id}"
    #     request_to_sql(sql_string)

    def orm_select(self, table_name=None, right_table_name=None, left_fk=None, right_id=None, fields='*', ordered_by=None):
        ordered = f'ORDERED_BY {table_name}.{ordered_by}' if ordered_by else ''
        if right_table_name:
            ordered = f'ORDERED_BY {table_name}.{ordered_by}' if ordered_by else ''
        else:
            sql_str = f'SELECT {fields} FROM {table_name}'
        return self.request_to_sql(sql_str)
