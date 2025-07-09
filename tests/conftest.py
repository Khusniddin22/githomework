import pytest

#Фикстуры с маскировкой номера карты/счета из модуля widget.py

@pytest.fixture
def visa_platinum():
    return 'Visa Platinum 7000 79** **** 6361'

@pytest.fixture
def type_account():
    return 'Счет **4305'

@pytest.fixture
def account_short():
    return 'Неправильно набран номер счета'

@pytest.fixture
def card_short():
    return 'Неправильно набран номер карты'

