import os

from dotenv import load_dotenv
import pyodbc

import SQL_Queries

load_dotenv()

DRIVER = os.getenv('MS_SQL_DRIVER')
SERVER = os.getenv('MS_SQL_SERVER')
WORK_DATABASE = os.getenv('MS_SQL_DATABASE')
PAD_DATABASE = os.getenv('MS_PAD_DATABASE')
USER = os.getenv('MS_SQL_USER')
PASSWORD = os.getenv('MS_SQL_KEY')

"""Простое подключение"""

connection_string = f'''DRIVER={{SQL Server}};
                SERVER={SERVER};
                DATABASE={PAD_DATABASE};
                Trusted_Connection=yes'''

"""Надежное соединение"""

# connection_string = f'''DRIVER={DRIVER};
#                 SERVER={SERVER};
#                 DATABASE={PAD_DATABASE};
#                 UID={USER};
#                 PWD={PASSWORD}'''

conn = pyodbc.connect(connection_string)
conn.autocommit = True

try:
    SQL_QUERY = SQL_Queries.create_database_default(WORK_DATABASE)
    conn.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f'Database {WORK_DATABASE} Created')
# finally:
#     conn.close()

cursor = conn.cursor()
table_name = 'Products'

try:
    SQL_QUERY = SQL_Queries.create_table(table_name)
    cursor.execute(fr'USE {WORK_DATABASE};')
    cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as ex:
    print(ex)
else:
    print(f'Table {table_name} created!!')
# finally:
#     conn.close()

try:
    SQL_QUERY = SQL_Queries.insert_data_products(table_name)
    cursor.execute(fr'USE {WORK_DATABASE};')
    cursor.execute(SQL_QUERY)
except pyodbc.ProgrammingError as PEex:
    print(PEex)
except pyodbc.IntegrityError as IEex:
    print(IEex)
else:
    print(f'Data in {table_name} inserted!!')
finally:
    conn.close()