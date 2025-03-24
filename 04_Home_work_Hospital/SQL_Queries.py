import json


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


"""SOME. Врачи, у которых премия выше средней премии по всем отделам."""


def some_query():
    QUERY = f"""SELECT Surname, Name
                FROM Doctors
                WHERE Premium > SOME (
                SELECT AVG(Premium)
                FROM Doctors);"""
    return QUERY


"""Врачи, у которых зарплата выше, чем у всех врачей в отделе "Кардиология"."""


def all_query():
    QUERY = f"""SELECT Surname, Name
                FROM Doctors
                WHERE Salary > ALL (
                SELECT Salary
                FROM Doctors
                WHERE DepartmentID = (
                SELECT Id
                FROM Departments
                WHERE DepartmentName = 'Кардиология'));"""
    return QUERY


"""ANY/SOME ALL. Врачи, у которых зарплата выше, чем у всех врачей в отделе "Кардиология", но ниже, чем у любого врача в отделе "Хирургия"."""


def any_some_all_query():
    QUERY = f"""SELECT Surname, Name
                FROM Doctors
                WHERE Salary > ALL (SELECT Salary
                                    FROM Doctors
                                    WHERE DepartmentID = (SELECT Id
                                                            FROM Departments
                                                            WHERE DepartmentName = 'Кардиология'))
                AND Salary < ANY (SELECT Salary
                                    FROM Doctors
                                    WHERE DepartmentID = (SELECT Id
                                                            FROM Departments
                                                            WHERE DepartmentName = 'Педиатрия'));"""
    return QUERY


"""UNION. Список врачей из отдела "Кардиология" и "Хирургия"""


def union_query():
    QUERY = f"""SELECT Surname, Name
                FROM Doctors
                WHERE DepartmentID = (
                    SELECT Id
                    FROM Departments
                    WHERE DepartmentName = 'Хирургия'
                )
                UNION
                SELECT Surname, Name
                FROM Doctors
                WHERE DepartmentID = (
                    SELECT Id
                    FROM Departments
                    WHERE DepartmentName = 'Неврология');"""
    return QUERY


"""UNION ALL. Список врачей из отдела "Кардиология" и "Хирургия", включая все дубликаты."""


def union_all_query():
    QUERY = f"""SELECT Surname, Name
                FROM Doctors
                WHERE DepartmentID = (
                    SELECT Id
                    FROM Departments
                    WHERE DepartmentName = 'Неврология'
                )
                UNION ALL
                SELECT Surname, Name
                FROM Doctors
                WHERE DepartmentID = (
                    SELECT Id
                    FROM Departments
                    WHERE DepartmentName = 'Терапия');"""
    return QUERY


"""INNER JOIN. список врачей с их отделами."""


def inner_join():
    QUERY = f"""SELECT D.Surname, D.Name, DE.DepartmentName
                FROM Doctors AS D
                INNER JOIN Departments AS DE ON D.DepartmentID = DE.Id;"""
    return QUERY


"""LEFT JOIN. Список всех отделов и соответствующих врачей, включая отделы без врачей."""


def left_join():
    # join_dict = {}
    QUERY = f"""SELECT Departments.DepartmentName, Doctors.Surname, Doctors.Name
                FROM Departments
                LEFT JOIN Doctors ON Departments.Id = Doctors.DepartmentID;
                """
    # join_dict = {'DepName':QUERY.DepartmentName,
    #              'Surname':QUERY.Surname,
    #              'Name':QUERY.Name}
    # with open('left_query.json', 'w',encoding='UTF-8') as f:
    #     json.dump(join_dict, f, ensure_ascii=False, indent=4)
    return QUERY

"""RIGHT JOIN. список всех врачей и их отделов, включая врачей без отделов."""
def right_join():
    QUERY = f"""SELECT Doctors.Surname, Doctors.Name, Departments.DepartmentName
                FROM Doctors
                RIGHT JOIN Departments ON Doctors.DepartmentID = Departments.Id;"""
    return QUERY