import json
import os


def financial_transactions(path_file: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(path_file, "r", encoding="utf-8") as f_tr:
            if f_tr is None:
                return []
            else:
                data = json.load(f_tr)
                return data
    except FileNotFoundError:
        return []


# получаем абсолютный путь к директории, содержащей utils.py
utils_path = os.path.dirname(os.path.abspath(__file__))

# получаем путь на 2 уровня выше чем utils файл
project_root_path = os.path.dirname(os.path.abspath(utils_path))

# объединяем путь к корню проекта с путем к файлу operations.json
abs_path_file = os.path.join(project_root_path, "data", "operations.json")

print(financial_transactions(abs_path_file))
