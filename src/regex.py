import re
from collections import Counter, defaultdict


list_transactions = [
                    {'id': '650703',
                     'state': 'EXECUTED',
                      'date': '2023-09-05T11:30:32Z',
                     'description': 'Перевод организации'
                      },
                     {'id': '3598919',
                      'state': 'EXECUTED',
                      'date': '2020-12-06T23:00:58Z',
                      'description': 'Открытие вклада'
                      },
                     {'id': '593027',
                      'state': 'CANCELED',
                      'date': '2023-07-22T05:02:01Z',
                      'description': 'Открытие вклада'
                      },
                     {'id': '4699552',
                      'state': 'EXECUTED',
                      'date': '2022-03-23T08:29:37Z',
                      'description': 'Перевод организации'
                      }
                     ]

def process_bank_search(data: list[dict], search: str)->list[dict]:
    list_of_found_transactions = []
    for transaction in data:
        for value in transaction.values():
            pattern = re.findall(search, value)
            if pattern:
                list_of_found_transactions.append(transaction)

    return list_of_found_transactions


def process_bank_operations(data: list[dict], categories:list)->dict:
    list_categories = []
    for transaction in data:
        if transaction['description'] in categories:
            list_categories.append(transaction['description'])
    return Counter(list_categories)