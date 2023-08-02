from abc import ABC, abstractmethod  # Abstract Basic Class это для абстрактного класса
import requests


class AbstractApi(ABC):
    """
    Абстрактный класс от которого всё наследуется
    """
    @abstractmethod
    def get_request(self, keyword):
        """
        Получить параметры в json-файле, подключившийсь к API
        :param keyword: Слово, которое вводит пользователь для поиска
        :return:
        """
        pass

    @abstractmethod
    def get_vacancies(self, keyword):
        """
        Получить вакансии
        :param keyword:
        :return:
        """
        pass


class HHApi(AbstractApi):
    def get_request(self, keyword):
        params = {
            "page": 0,
            "per_page": 50,
            "text": keyword
        }
        data = requests.get("https://api.hh.ru/vacancies", params=params).json()
        return data["items"]

    def get_vacancies(self, keyword):
        data = self.get_request(keyword)
        all_vacancies = []
        for vacancy in data:
            name = vacancy["name"]
            url = vacancy["alternate_url"]
            if vacancy["salary"]:
                salary_min = vacancy["salary"]["from"] if vacancy["salary"]["from"] else 0
                salary_max = vacancy["salary"]["to"] if vacancy["salary"]["to"] else 0
            else:
                salary_min = 0
                salary_max = 0
            company = vacancy["employer"]["name"]
            place_of_work = vacancy["address"]["city"]
            all_vacancies.append({
                "name": name,
                "url": url,
                "salary_min": salary_min,
                "salary_max": salary_max,
                "company": company,
                "place_of_work": place_of_work
            })
        return all_vacancies


class SJApi(AbstractApi):
    def get_request(self, keyword):
        params = {
            "page": 0,
            "count": 50,
            "keyword": keyword
        }
        headers = {"X-Api-App-Id": "v3.r.137720533.801807ff4e2400fd44a43ce74a23e0d301cb34b6.db2dece0b1015843fc43bae6416a526b745f0320"}
        data = requests.get("https://api.superjob.ru/2.0/vacancies/", params=params, headers=headers).json()
        return data["objects"]

    def get_vacancies(self, keyword):
        data = self.get_request(keyword)
        all_vacancies = []
        for vacancy in data:
            profession = vacancy["profession"]
            url = vacancy["url"]

            salary_min = vacancy["payment_from"] if vacancy["payment_from"] else 0
            salary_max = vacancy["payment_to"] if vacancy["payment_to"] else 0


            company = vacancy["firm_name"]
            place_of_work = vacancy["town"]["title"]
            all_vacancies.append({
                "name": profession,
                "url": url,
                "salary_min": salary_min,
                "salary_max": salary_max,
                "company": company,
                "place_of_work": place_of_work
            })
        return all_vacancies
        pass

