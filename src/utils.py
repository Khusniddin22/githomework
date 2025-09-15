import json
import os
import logging


logger_utils = logging.getLogger('utils')
logger_utils.setLevel(logging.DEBUG)
file_handler = logging.FileHandler('logs/utils.log')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)


def financial_transactions(path_file: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    try:
        with open(path_file, "r", encoding="utf-8") as f_tr:
            if f_tr is None:
                logger_utils.warning(f'Файл {path_file} не открыт. Возвращается пустой список."')
                return []
            else:
                data = json.load(f_tr)
                logger_utils.info(f"Файл {path_file} успешно загружен.")
                return data
    except FileNotFoundError:
        logger_utils.error(f'Файл {path_file} не найден. Возвращается пустой список.')
        return []
    except json.JSONDecodeError:
        logger_utils.error(f"Некорректный формат JSON в файле {path_file}. Возвращается пустой список.")
        return []


# получаем абсолютный путь к директории, содержащей utils.py
utils_path = os.path.dirname(os.path.abspath(__file__))

# получаем путь на 2 уровня выше чем utils файл
project_root_path = os.path.dirname(os.path.abspath(utils_path))

# объединяем путь к корню проекта с путем к файлу operations.json
abs_path_file = os.path.join(project_root_path, "data", "operations.json")

print(financial_transactions(abs_path_file))
