from masks import get_mask_card_number
from masks import get_mask_account


def mask_account_card(type_and_account_card: str) -> str:
    """Функция принимает номер карты или счета и возвращает замаскированный номер"""
    account_card = ""
    mask_account = ""
    type_name = ""
    for symbol in type_and_account_card:  # отбрасываем тип и оставляем только номер
        if symbol.isdigit():
            account_card += symbol
        else:
            type_name += symbol

    if len(account_card) == 20:  # проверка на номер счета
        mask_account = get_mask_account(int(account_card))
    else:  # иначе это номер карты
        mask_account = get_mask_card_number(int(account_card))

    return type_name + mask_account


def get_date(long_date: str) -> str:
    """Функция возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    correct_date = long_date[8:10] + "." + long_date[5:7] + "." + long_date[:4]
    return correct_date
