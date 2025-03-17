import json

import requests


class HH:
    employers_data = []
    vacancies_emp = []

    def __init__(self, employer):
        self.employer = employer
        self.employer_dict = {}

    def get_employer(self):
        url = r'https://api.hh.ru/employers'
        params = {'text': {self.employer}, 'areas': 113, 'per_page': 20}
        respons = requests.get(url, params)
        employer = respons.json()
        if not employer:
            print('dfdffs')
            return False
        elif not employer['items']:
            print('нет указанных работодателей')
            return False
        else:
            for emp in employer['items']:
                self.employer_dict = {
                    'id': emp['id'],
                    'name': emp['name'],
                    'alternate_url':emp['alternate_url']
                }
                HH.employers_data.append(self.employer_dict)
            self.employer_dict = {
                'id': employer['items'][0]['']
            }
        return employer, respons

    def get_page_vacancies(self, employer_id, page):
        params = {
            'emploers_id': employer_id,
            'area': 113,
            'per_page':100,
            'page':page
        }
        response = requests.get('https://api.hh.ru/vacancies')
        data = response.content.decode()
        response.close()
        return data

    def get_vacancies(self, employer_id):
        vacancies_emp_dicts = []
        for page in range(10):
            vacancies_data = json.loads(self.get_page_vacancies(employer_id,page))




if __name__ == '__main__':
    hh = HH('skyeng')
    print(hh.get_employer()[0])
    print(hh.get_employer()[1])
    print(HH.employers_data)
