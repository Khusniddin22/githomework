import json


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


abs_path_file = r"C:\Users\79623\Desktop\home_work\githomework\data\operations.json"

print(financial_transactions(abs_path_file))
