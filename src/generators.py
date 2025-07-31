from typing import Dict, Iterator, List


def filter_by_currency(dict_of_transactions: List[Dict], valut: str) -> Iterator[Dict]:
    """Фильтрует список словарей транзакций и возвращает итератор,
    содержащий транзакции с указанной валютой."""
    return filter(lambda x: x["operationAmount"]["currency"]["code"] == valut, dict_of_transactions)


def transaction_descriptions(transactions: List[Dict]):
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for description in transactions:
        yield description["description"]


def card_number_generator(start: int, stop: int):
    """Ф-ия генерирует номера карт в заданном диапазоне"""
    for x in range(start, stop + 1):
        number = f"{x:016d}"
        formatted_number = " ".join([number[i : i + 4] for i in range(0, 16, 4)])
        yield formatted_number
