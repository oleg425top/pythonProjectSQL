import os
import json

import pyodbc
from dotenv import load_dotenv

import SQL_Queries


class ConnectHospital:
    @classmethod
    def connect_to_db(cls, driver, server, database, user, password):
        connection_string = f'''DRIVER={driver};
                                SERVER={server};
                                DATABASE={database};
                                UID={user};
                                PWD={password};'''
        try:
            conn = pyodbc.connect(connection_string)
            conn.autocommit = True
        except pyodbc.ProgrammingError as ex:
            print(ex)
        else:
            return conn

    @classmethod
    def close_connection(cls, conn_obj):
        conn_obj.close()


class MSSQLOperator:

    def __init__(self, conn_obj):
        self.conn = conn_obj
        self.conn_cursor = self.conn.cursor()

    def create_table(self, database_name, sql_query, table_name=None, references_table=None, references_column=None):
        self.conn_cursor.execute(f'USE {database_name}')
        SQLQuery = sql_query(table_name)
        try:
            self.conn_cursor.execute(SQLQuery)
        except pyodbc.ProgrammingError as exPE:
            print(exPE)

            return False
        except pyodbc.OperationalError as exOE:
            print(exOE)

            return False
        else:
            print(f'Таблица {table_name} успешно создана!')

            return True

    def drop_table(self, database_name, sql_query, table_name):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query(table_name)
        try:
            self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            print(f'Таблица {table_name} успешно удалена!')
            return True

    def get_data_from_any_table(self, database_name, sql_query, table_name=None):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query(table_name)
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for rec in records:
                print(rec)
            return True

    def first_exists_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'DepartmentName': record.DepartmentName}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/first_exists_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def second_exists_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'FullName': record.FullName}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/second_exists_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def any_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'FullName': record.FullName}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/any_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def some_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/some_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def all_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/all_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def any_some_all_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/any_some_all_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def union_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/union_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def union_all_query(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/union_all_query.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def inner_join(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name, 'DepartmentName': record.DepartmentName}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/inner_join.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def left_join(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name, 'DepartmentName': record.DepartmentName}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/left_join.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True

    def right_join(self, database_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQL_Query = sql_query()
        data_list = []
        try:
            result = self.conn_cursor.execute(SQL_Query)
        except pyodbc.Error as ex:
            print(ex)
            return False
        else:
            records = result.fetchall()
            for record in records:
                data_dict = {'Surname': record.Surname, 'Name': record.Name, 'DepartmentName': record.DepartmentName}
                data_list.append(data_dict)
            print(data_list)
            with open('Json_data/right_join.json', 'w', encoding='utf-8') as fp:
                json.dump(data_list, fp, ensure_ascii=False, indent=4)
                print('Data added to json file')
            return True


if __name__ == '__main__':
    load_dotenv()

    DRIVER = os.getenv('MS_SQL_DRIVER')
    SERVER = os.getenv('MS_SQL_SERVER')
    WORK_DATABASE = "Hospital"
    PAD_DATABASE = os.getenv('MS_PAD_DATABASE') #в данном примере не используется!!
    USER = os.getenv('MS_SQL_USER')
    PASSWORD = os.getenv('MS_SQL_KEY')

    conn = ConnectHospital.connect_to_db(driver=DRIVER, server=SERVER, user=USER, password=PASSWORD,
                                         database=WORK_DATABASE)

    my_db_operator = MSSQLOperator(conn)
    table_name = input('Ведите название таблицы')
    my_db_operator.create_table(WORK_DATABASE, SQL_Queries.create_table, table_name)
    my_db_operator.drop_table(WORK_DATABASE, SQL_Queries.drop_table, table_name)
    my_db_operator.first_exists_query(WORK_DATABASE, SQL_Queries.first_exists_query)
    print()
    my_db_operator.get_data_from_any_table(WORK_DATABASE, SQL_Queries.universal_query)
    my_db_operator.second_exists_query(WORK_DATABASE, SQL_Queries.second_exists_query)
    my_db_operator.any_query(WORK_DATABASE, SQL_Queries.any_query)
    print()
    my_db_operator.some_query(WORK_DATABASE, SQL_Queries.some_query)
    print()
    my_db_operator.all_query(WORK_DATABASE, SQL_Queries.all_query)
    my_db_operator.any_some_all_query(WORK_DATABASE, SQL_Queries.any_some_all_query)
    print()
    my_db_operator.union_query(WORK_DATABASE, SQL_Queries.union_query)
    print()
    my_db_operator.union_all_query(WORK_DATABASE, SQL_Queries.union_all_query)
    print()
    my_db_operator.inner_join(WORK_DATABASE, SQL_Queries.inner_join)
    print()
    my_db_operator.left_join(WORK_DATABASE, SQL_Queries.left_join)
    print()
    my_db_operator.right_join(WORK_DATABASE, SQL_Queries.right_join)
    print()
