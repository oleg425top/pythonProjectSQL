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
            self.conn.close()
            return False
        else:
            self.conn.close()
            print(f'База данных {database_name} успешно создана')


    def create_table(self, database_name, table_name, sql_query):
        self.conn_cursor.execute(f'USE {database_name}')
        SQLQuery = sql_query(table_name)
        try:
            self.conn_cursor.execute(SQLQuery)
        except pyodbc.ProgrammingError as exPE:
            print(exPE)
            self.conn.close()
            return False
        except pyodbc.OperationalError as exOE:
            print(exOE)
            self.conn.close()
            return False
        else:
            print(f'Таблица {table_name} успешно создана!')
            self.conn.close()
            return True


