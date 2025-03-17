import os

import pyodbc
from dotenv import load_dotenv

import SQL_Queries


class ConnectDB:
    @classmethod
    def connect_to_db(cls, driver, server, pad_database, user, password):
        connection_string = f'''DRIVER={driver};
                        SERVER={server};
                        DATABASE={pad_database};
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

    def create_database_params(self, database_name, size='8', maxsize='16', filegrowth='10%'):
        SQLCommand = SQL_Queries.create_database(database_name, size, maxsize, filegrowth)
        try:
            self.conn.execute(SQLCommand)
        except pyodbc.ProgrammingError as ex:
            print(ex)

            return False
        else:

            print(f'База данных {database_name} успешно создана')

    def create_table(self, database_name, sql_query, table_name, references_table=None, references_column=None):
        self.conn_cursor.execute(f'USE {database_name}')
        SQLQuery = sql_query(table_name, references_table, references_column)
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


if __name__ == '__main__':
    load_dotenv()

    DRIVER = os.getenv('MS_SQL_DRIVER')
    SERVER = os.getenv('MS_SQL_SERVER')
    WORK_DATABASE = "EmployersVacancies425"
    PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
    USER = os.getenv('MS_SQL_USER')
    PASSWORD = os.getenv('MS_SQL_KEY')

    my_conn = ConnectDB.connect_to_db(driver=DRIVER, server=SERVER, pad_database=PAD_DATABASE, user=USER,
                                      password=PASSWORD)
    my_db_operator = MSSQLOperator(my_conn)
    my_db_operator.create_database_params(WORK_DATABASE, '10', '20', '5%')
    my_db_operator.drop_table(WORK_DATABASE, SQL_Queries.drop_table, 'Vacancies')
    my_db_operator.drop_table(WORK_DATABASE, SQL_Queries.drop_table, 'Employers')
    my_db_operator.create_table(WORK_DATABASE, SQL_Queries.create_table_employers, 'Employers')
    my_db_operator.create_table(WORK_DATABASE, SQL_Queries.create_table_vacancies, table_name='Vacancies',
                                references_table='Employers', references_column='id')
