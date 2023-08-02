class Vacancy:
    """
    Класс для показа вакансии
    """

    all = []

    def __init__(self, profession, salary_from, salary_to, vacancy_url, company, place_of_work):
        """
        Инициализирует атрибуты экземпляра класса Vacancy
        :param profession: название должности
        :param salary_from: нижний предел зарплаты
        :param salary_to: верхний предел зарплаты
        :param vacancy_url: ссылка на вакансию
        :param company: Название компании
        :param place_of_work: адрес работы
        """
        self.__name = profession
        self.__salary_from = salary_from
        self.__salary_to = salary_to
        self.__vacancy_url = vacancy_url
        self.__company = company
        self.__place_of_work = place_of_work

        self.all.append(self)

    def __str__(self):
        """Выведем информацию в адекватном виде"""
        return f"""Вакансия: {self.name}
Url: {self.vacancy_url}
ЗП: От {self.salary_from} до {self.__salary_to}
Компания: {self.company}"""

    def __le__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from <= other.__salary_from

    def __lt__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from < other.__salary_from

    def __eq__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from == other.__salary_from

    def __ge__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from >= other.__salary_from

    def __gt__(self, other):
        """
        Сравнивает вакансии между собой по зарплате
        :param other: объект класса Vacancy
        :return: bool
        """
        return self.__salary_from > other.__salary_from

    @property
    def name(self):
        return self.__name

    @property
    def salary_from(self):
        return self.__salary_from

    @property
    def salary_to(self):
        return self.__salary_to

    @property
    def vacancy_url(self):
        return self.__vacancy_url

    @property
    def company(self):
        return self.__company

    @property
    def place_of_work(self):
        return self.__place_of_work


    @classmethod
    def add_to_class(cls, vacancies_data):
        """
        Инициализирует экземпляры класса Vacancy, иначе говоря, отсортирует
        :param vacancies_data: данные о вакансиях
        """
        if vacancies_data:
            for vacancy in vacancies_data:
                cls(vacancy['name'], vacancy['salary_min'], vacancy['salary_max'], vacancy['url'],
                    vacancy["company"], vacancy["place_of_work"])



