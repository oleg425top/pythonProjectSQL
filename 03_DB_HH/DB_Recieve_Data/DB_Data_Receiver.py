from EngineHH import HH

import json


class DataReceiver:

    def __init__(self, employers: list):
        self.employers = employers

    def get_employers_data(self):
        for employer in self.employers:
            HH(employer).get_employer()
        return HH.employers_data

    def get_vacancies_data(self):
        vacancies = []
        employers = self.get_employers_data()
        for i in range(len(employers)):
            vacancies.append(HH(self.employers[i]).get_vacancies(employers[i]['id']))
        vacancies = DataReceiver.normalize_vacancies(vacancies)
        vacancies = DataReceiver.normalize_salary(vacancies)
        return vacancies

    @staticmethod
    def normalize_vacancies(vacancies):
        all_vacancies = []
        for vacancy_emp in vacancies:
            all_vacancies.extend(vacancy_emp)
        return all_vacancies

    @staticmethod
    def normalize_salary(vacancies):
        for vacancy in vacancies:
            if vacancy['salary_from'] is None:
                vacancy['salary_from'] = 'NULL'
            if vacancy['salary_to'] is None:
                vacancy['salary'] = 'NULL'
        return vacancies


if __name__ == '__main__':
    employers = ['skyeng']
    my_data_receiver = DataReceiver(employers)
    my_employers = my_data_receiver.get_employers_data()
    my_vacancies = my_data_receiver.get_vacancies_data()
    print(my_vacancies)
