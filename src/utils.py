import json
import logging
import os

logger_utils = logging.getLogger("utils")
logger_utils.setLevel(logging.DEBUG)  # Устанавливаем уровень логирования
os.makedirs("logs", exist_ok=True)
file_handler = logging.FileHandler("logs/utils.log")  # Указываем путь к файлу логов
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)  # Добавляем обработчик к логгеру


def financial_transactions(path_file: str) -> list:
    """
    Функция, которая принимает на вход путь до JSON-файла и
    возвращает список словарей с данными о финансовых транзакциях.
    """
    logger_utils.debug(f"Вызвана функция financial_transactions с аргументом: {path_file}")

    try:
        # Проверяем, что загруженные данные являются списком
        if not os.path.exists(path_file):
            logger_utils.error(f"Файл {path_file} не найден. Возвращается пустой список.")
            return []

        with open(path_file, "r", encoding="utf-8") as f_tr:
            data = json.load(f_tr)
            if data is None:
                logger_utils.warning(f"Файл {path_file} содержит null. Возвращается пустой список.")
                return []
            if not isinstance(data, list):
                logger_utils.warning(
                    f"Файл {path_file} содержит данные не в формате списка. Возвращается пустой список."
                )
                return []

            logger_utils.info(f"Файл {path_file} успешно загружен.")
            return data
    except json.JSONDecodeError:
        logger_utils.error(f"Некорректный формат JSON в файле {path_file}. Возвращается пустой список.")
        return []
    except Exception as e:
        logger_utils.error(
            f"Произошла непредвиденная ошибка при чтении файла {path_file}: {e}. Возвращается пустой список."
        )
        return []
