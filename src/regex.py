import re

list_transactions = [
                    {'id': '650703',
                     'state': 'EXECUTED',
                      'date': '2023-09-05T11:30:32Z'
                      },
                     {'id': '3598919',
                      'state': 'EXECUTED',
                      'date': '2020-12-06T23:00:58Z',
                      },
                     {'id': '593027',
                      'state': 'CANCELED',
                      'date': '2023-07-22T05:02:01Z',
                      }
                     ]

def process_bank_search(data: list[dict], search: str)->list[dict]:
    list_of_found_transactions = []
    for tranaction in data:
        for value in tranaction.values():
            pattern = re.findall(search, value)
            if pattern:
                list_of_found_transactions.append(tranaction)

    return list_of_found_transactions

print(process_bank_search(list_transactions, 'EXECUTED'))