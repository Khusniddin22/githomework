# Банковское приложение

## Описание

Данный проект предназначен для маскировки номеров карт и счетов клиента. Он обеспечивает безопасность конфиденциальной информации, позволяя скрыть часть данных при их отображении. Также данный проект позволяет отсортировывает списки по заданному ключу.

## Установка

1. Клонируйте репозиторий:
```
git clone https://github.com/Khusniddin22/githomework.git
```

## Использование

### Маскировка номера карты и счета

Для маскировки номера карты используйте функцию mask_account_card(type_and_account_card), которая принимает номер карты в виде строки и возвращает замаскированный номер.

### Пример маскировки карты
```
masked_card = mask_account_card("Visa Platinum 7000792289606361")
print(masked_card)
```
Вывод
```
Visa Platinum 7000 79** **** 6361
```

### Пример маскировки счета
```
masked_account = mask_account_card("Счет 73654108430135874305")
print(masked_account)
```
Вывод
```
Счет **4305
```
## Тесты
Были протестированы все функции программы
использован фреймворк pytest

### Примеры использования:

1. Тесты с функцией get_mask_number
```
from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_number():
    assert get_mask_account(73654108430135874305) == '**4305'
    assert get_mask_account(73654108430135874.305) == None
    assert get_mask_account(7365410) == None
```
2. Тесты функции mask_account_card c использованием фикстуры

Фикстура в модуле conftest.py:
```
@pytest.fixture
def visa_platinum():
    return 'Visa Platinum 7000 79** **** 6361'
```
Тест в модуле test_widget.py
```
import pytest

from src.widget import mask_account_card, get_date

def test_mask_account_card_visa(visa_platinum):
    assert mask_account_card('Visa Platinum 7000792289606361') == visa_platinum

def test_mask_account_card_type_account(type_account):
    assert mask_account_card('Счет 73654108430135874305') == type_account
```

3. Тесты с функцией filter_by_state с использованием параметризации
```
@pytest.mark.parametrize('list_of_dicts, state, result_list', [
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
        ],
        'EXECUTED',
        [{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'}]
    ),
    (
        [
            {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
        ],
        'CANCELED',
        [
            {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'}
        ]
    ),
    (
        [
            {'id': 41428829, 'state': '', 'date': '2019-07-03T18:35:29.512364'},
            {'id': 615064591, 'state': '', 'date': '2018-10-14T08:21:33.419441'},
            {'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'}
        ],
        'EXECUTED',
        [{'id': 594226727, 'state': 'EXECUTED', 'date': '2018-09-12T21:27:25.241689'}]
    ),
])

def test_filter_by_state(list_of_dicts, state, result_list):
    assert filter_by_state(list_of_dicts, state) == result_list
```

## Генераторы списков
Были созданы и протестированы функции-генераторы и генераторные выражения

###Примеры использования:

1. filter_by_currency, которая принимает на вход список словарей, представляющих транзакции.

```
for _ in range(2):
    print(next(usd_transactions))

>>> {
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
      {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
```

2. transaction_descriptions, который принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.

```
descriptions = transaction_descriptions(transactions)
for _ in range(5):
    print(next(descriptions))

>>> Перевод организации
    Перевод со счета на счет
    Перевод со счета на счет
    Перевод с карты на карту
    Перевод организации
```

3. card_number_generator, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты. Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.

```
for card_number in card_number_generator(1, 5):
    print(card_number)

>>> 0000 0000 0000 0001
    0000 0000 0000 0002
    0000 0000 0000 0003
    0000 0000 0000 0004
    0000 0000 0000 0005
```