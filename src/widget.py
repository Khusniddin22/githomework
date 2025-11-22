from src.masks import get_mask_account, get_mask_card_number, get_mask_account_zero, get_mask_card_number_zero


def mask_account_card(type_and_account_card: str) -> str:
    """Функция принимает номер карты или счета
    и возвращает замаскированный номер"""
    account_card = ""
    type_name = ""
    for symbol in type_and_account_card:  # отбрасываем тип и оставляем только номер
        if symbol.isdigit():
            account_card += symbol
        else:
            type_name += symbol

    if len(account_card) == 20:  # проверка на номер счета
        if account_card[0] == '0':
            mask_account = get_mask_account_zero(account_card)
        else:
            mask_account = get_mask_account(int(account_card))
    elif len(account_card) == 16:  # иначе это номер карты
        if account_card[0] == '0':
            mask_account = get_mask_card_number_zero(account_card)
        else:
            mask_account = get_mask_card_number(int(account_card))
    else:
        if type_name == "Счет ":
            return "Неправильно набран номер счета"
        else:
            return "Неправильно набран номер карты"
    return type_name + str(mask_account)


def get_date(long_date: str) -> str:
    """Функция возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    day = long_date[8:10]
    month = long_date[5:7]
    year = long_date[:4]
    if not day.isdigit() or not month.isdigit() or not year.isdigit():
        raise ValueError("Неправильный формат даты")
    if day.isdigit() or month.isdigit() or year.isdigit():
        if int(day) < 1 or int(month) > 13 or int(day) > 31:
            raise ValueError("Неправильный формат даты")
    correct_date = day + "." + month + "." + year
    return correct_date

p = '0'
if p.isdigit():
    print('yes')