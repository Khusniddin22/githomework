import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функция, принимающая список словарей с данными о банковских операциях и строку поиска
     и возвращающая список словарей, в описании которых есть данная строка
    """
    list_of_found_transactions = []
    for transaction in data:
        if "description" in transaction and re.search(search, transaction["description"]):
            list_of_found_transactions.append(transaction)

    return list_of_found_transactions


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Функция, которая принимает список словарей с данными о банковских операциях
    и список категорий операций и возвращает словарь категорий и количество операций в каждой категории
    """
    list_categories = []
    for transaction in data:
        if transaction["description"] in categories:
            list_categories.append(transaction["description"])
    return Counter(list_categories)
