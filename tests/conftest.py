import pytest

# Фикстуры с маскировкой номера карты/счета из модуля widget.py


@pytest.fixture
def visa_platinum():
    return "Visa Platinum 7000 79** **** 6361"


@pytest.fixture
def type_account():
    return "Счет **4305"


@pytest.fixture
def account_short():
    return "Неправильно набран номер счета"


@pytest.fixture
def card_short():
    return "Неправильно набран номер карты"


@pytest.fixture
def identical_dates():
    return [
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def filter_by_currency_usd():
    return {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
            "description": "Перевод организации",
            "from": "Счет 75106830613657916952",
            "to": "Счет 11776614605963066702",
    }

