import json
from src.vacancy import Vacancy


class JSONSaver:
    def __init__(self):
        self.filename = "vacancies.json"

    def save_vacancies(self, data):
        """
        Записывает в файл с отступами информацию
        :param data:
        :return:
        """
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def get_vacancies(self):
        """
        Вытащить из файла данные
        :return:
        """
        with open(self.filename, encoding="utf-8") as f:
            return json.load(f)




