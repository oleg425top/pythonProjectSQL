def create_database_default(name):
    COMMAND = fr'CREATE DATABASE {name};'
    return COMMAND


def create_database(name, size, maxsize, filegrowth):
    QUERY = fr"""
    CREATE DATABASE {name}
    ON
    (NAME = {name}Database_data,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\{name}Database_data.mdf',
    SIZE = {size}MB,
    MAXSIZE = {maxsize}GB,
    FILEGROWTH = {filegrowth})
    LOG ON
    (NAME = {name}Database_log,
    FILENAME = 'C:\Program Files\Microsoft SQL Server\MSSQL16.SQLEXPRESS\MSSQL\DATA\{name}Database_data.ldf',
    SIZE = {size}MB,
    MAXSIZE = {str(round(int(maxsize) * 0.1))}GB,
    FILEGROWTH = {filegrowth})
    """
    return QUERY


def create_table_employers(table_name, references_table =None, references_column=None):
    QUERY = f"""CREATE TABLE {table_name}
                (id int PRIMARY KEY,
                employer_name nvarchar(200),
                employer_url nvarchar(200));"""
    return QUERY

def create_table_vacancies(table_name, references_table, references_column):
    QUERY = f"""CREATE TABLE {table_name}
                (id int PRIMARY KEY,
                vacancy_city nvarchar(200),
                vacancy_name nvarchar(200),
                vacancy_url nvarchar(200),
                vacancy_salary_from money,
                vacancy_salary_to money,
                employer_id int REFERENCES {references_table} ({references_column}));"""
    return QUERY

def drop_table(table_name):
    QUERY = f"DROP TABLE {table_name}"
    return QUERY
