def get_mask_card_number(card_number: int) -> str:
    """Функция для маскировки номера карты"""
    card_number_str = str(card_number)
    mask_card_nuber = ""
    count_number = 0
    for i in range(len(card_number_str)):
        count_number += 1
        if count_number == 5:
            mask_card_nuber += " "
            count_number = 1
        if i >= 6 and i <= 11:
            mask_card_nuber += "*"
        else:
            mask_card_nuber += card_number_str[i]
    return mask_card_nuber


def get_mask_account(account_number: int) -> str:
    """Функция маскирует номер счета и и отображает в формате **XXXX"""
    account_number_str = str(account_number)
    mask_account_number = "**" + account_number_str[-4:]
    return mask_account_number
