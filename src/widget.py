def mask_account_card(type_and_account_card: str) -> str:
    """Функция принимает номер карты или счета и возвращает замаскированный номер"""
    account_card = ""
    mask_account = ""
    type_name = ""
    count_digit = 0
    for symbol in type_and_account_card:  # отбрасываем тип и оставляем только номер
        if symbol.isdigit():
            account_card += symbol
        else:
            type_name += symbol

    if len(account_card) == 20:  # проверка на номер счета
        mask_account = "**" + account_card[-4:]
    else:  # иначе это номер карты
        for i in range(len(account_card)):
            count_digit += 1
            if count_digit == 5:
                mask_account += " "
                count_digit = 1
            if i >= 6 and i <= 11:
                mask_account += "*"
            else:
                mask_account += account_card[i]

    return type_name + mask_account


def get_date(long_date: str) -> str:
    """Функция возвращает дату в формате 'ДД.ММ.ГГГГ'"""
    correct_date = long_date[8:10] + "." + long_date[5:7] + "." + long_date[:4]
    return correct_date
