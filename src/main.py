# # Создание экземпляра класса для работы с API сайтов с вакансиями
# hh_api = HeadHunterAPI()
# superjob_api = SuperJobAPI()
#
# # Получение вакансий с разных платформ
# hh_vacancies = hh_api.get_vacancies("Python")
# superjob_vacancies = superjob_api.get_vacancies("Python")
#
# # Создание экземпляра класса для работы с вакансиями
# vacancy = Vacancy("Python Developer", "<https://hh.ru/vacancy/123456>", "100 000-150 000 руб.", "Требования: опыт работы от 3 лет...")
#
# # Сохранение информации о вакансиях в файл
# json_saver = JSONSaver()
# json_saver.add_vacancy(vacancy)
# json_saver.get_vacancies_by_salary("100 000-150 000 руб.")
# json_saver.delete_vacancy(vacancy)
#
# # Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter", "SuperJob"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     filtered_vacancies = filter_vacancies(hh_vacancies, superjob_vacancies, filter_words)
#
#     if not filtered_vacancies:
#         print("Нет вакансий, соответствующих заданным критериям.")
#         return
#
#     sorted_vacancies = sort_vacancies(filtered_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)
#
#
# if __name__ == "__main__":
#     user_interaction()

from src.api_classes import HHApi
from src.jsonsaver import JSONSaver
from src.vacancy import Vacancy
from src.api_classes import SJApi

keyword = input("Введите слово для поиска вакансий")
hh = HHApi()
sj = SJApi()

vacancies = hh.get_vacancies(keyword)
sj_vacancies = sj.get_vacancies(keyword)
vacancies.extend(sj_vacancies)

jsonsaver = JSONSaver()
jsonsaver.save_vacancies(vacancies)
Vacancy.add_to_class(vacancies)
data = Vacancy.all
while True:
    print("1: Вывод всех вакансий")
    print("2: Вывод отсортированных вакансий")
    print("3: Вывод топа вакансий")
    print("4: Выход")
    answer = input()
    if answer == "1":
        for vacancy in data:
            print(vacancy)
            print("-" * 100)
    elif answer == "2":
        Vacancy.all = sorted(Vacancy.all)
        for vacancy in Vacancy.all:
            print(vacancy)
            print("-" * 100)
    elif answer == "3":
        Vacancy.all = sorted(Vacancy.all, reverse=True)
        top = int(input("Введите кол-во вакансий"))
        for vacancy in Vacancy.all[:top]:
            print(vacancy)
            print("-" * 100)
    elif answer == "4":
        break