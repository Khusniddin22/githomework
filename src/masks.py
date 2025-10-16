import json
import os
import logging


logger_masks = logging.getLogger('masks')
logger_masks.setLevel(logging.DEBUG) # Устанавливаем уровень логирования
file_handler = logging.FileHandler('logs/masks.log') # Указываем путь к файлу логов
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s') # Формат логов
file_handler.setFormatter(file_formatter)  # Устанавливаем форматтер для обработчика
logger_masks.addHandler(file_handler)  # Добавляем обработчик к логгеру


def get_mask_card_number(card_number: int) -> str:
    """Функция для маскировки номера карты"""
    logger_masks.debug(f"Вызвана get_mask_card_number с аргументом: {card_number}")
    card_number_str = str(card_number)
    mask_card_nuber = ""
    count_number = 0
    if len(card_number_str) == 16:
        for i in range(len(card_number_str)):
            count_number += 1
            if count_number == 5:
                mask_card_nuber += " "
                count_number = 1
            if i >= 6 and i <= 11:
                mask_card_nuber += "*"
            else:
                mask_card_nuber += card_number_str[i]
        logger_masks.info(f"Успешно замаскирован номер карты: {card_number}")
        return mask_card_nuber
    else:
        logger_masks.error(f"Неправильно набран номер карты: {card_number}")
        return "Неправильно набран номер карты"


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счета и и отображает в формате **XXXX"""
    logger_masks.debug(f"Вызвана get_mask_account с аргументом: {account_number}")
    if len(str(account_number)) == 20:
        account_number_str = str(account_number)
        mask_account_number = "**" + account_number_str[-4:]
        logger_masks.info(f"Успешно замаскирован номер счета: {account_number}")
        return mask_account_number
    else:
        logger_masks.error(f"Неправильная длина номера счета: {account_number}")
        return None


print(get_mask_card_number(7000792289606361))
