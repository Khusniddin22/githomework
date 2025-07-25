from typing import Dict, List, Iterator


def filter_by_currency(dict_of_transactions: List[Dict], valut: str) -> Iterator[Dict]:
    """Фильтрует список словарей транзакций и возвращает итератор,
    содержащий транзакции с указанной валютой."""
    return filter(lambda x: x['operationAmount']['currency']['code'] == valut, dict_of_transactions)


transactions = [
    {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
    },
    {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "EUR",
                      "code": "EUR"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
    },
    {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
    }
]



def transaction_descriptions(transactions: List[Dict]):
    """Генератор, который принимает список словарей с транзакциями
    и возвращает описание каждой операции по очереди"""
    for description in transactions:
        yield description['description']


def card_number_generator(start: int, stop: int):
    """Ф-ия генерирует номера карт в заданном диапазоне"""
    for x in range(start, stop+1):
        number = f'{x:016d}'
        formatted_number = ' '.join([number[i:i+4] for i in range(0, 16, 4)])
        yield formatted_number

