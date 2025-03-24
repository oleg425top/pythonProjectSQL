def create_table(table_name):
    # table_name = input('Ведите название таблицы')
    query_list = []
    while True:
        column = input('Введите команду для создания колонки, либо введите stop!')
        if column == 'stop':
            break
        query_list.append(column)
    QUERY = f"""CREATE TABLE {table_name}
                ({(",".join(tuple(query_list)))});"""
    return QUERY


def drop_table(table_name):
    QUERY = f"DROP TABLE {table_name}"
    return QUERY


"""Выводит все данные из любой таблицы"""


def universal_query(table_name):
    table_name = input('Введите название таблицы')
    QUERY = f'SELECT * FROM {table_name}'
    return QUERY


"""EXISTS_1. Этот запрос вернет названия отделов, в которых есть хотя бы один врач."""


def first_exists_query():
    QUERY = f"""SELECT
                DepartmentName
                FROM
                Departments
                WHERE EXISTS(
                SELECT 1 FROM
                Doctors
                WHERE
                Doctors.DepartmentID = Departments.Id
                );"""
    return QUERY


"""EXISTS_2. Этот запрос вернет фамилии и имена врачей, у которых есть записи в расписании."""


def second_exists_query():
    QUERY = f"""SELECT Surname + ' ' + Name AS FullName
                FROM Doctors AS D
                WHERE EXISTS (
                SELECT 1
                FROM DoctorsExaminations AS DE
                WHERE DE.DoctorId = D.Id
                );"""
    return QUERY


"""ANY. Врачи, у которых зарплата выше средней зарплаты по всем отделам."""


def any_query():
    QUERY = f"""SELECT Surname + ' ' + Name AS FullName
                FROM Doctors AS D
                WHERE Salary > ANY(
                SELECT AVG(Salary)
                FROM Doctors);"""
    return QUERY
