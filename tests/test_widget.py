import pytest

from src.widget import mask_account_card, get_date


def test_mask_account_card_visa(visa_platinum):
    assert mask_account_card("Visa Platinum 7000792289606361") == visa_platinum


def test_mask_account_card_type_account(type_account):
    assert mask_account_card("Счет 73654108430135874305") == type_account


def test_mask_account_card_account_short(account_short):
    assert mask_account_card("Счет 736541084") == account_short


def test_mask_account_card_card_short(card_short):
    assert mask_account_card("Visa Platinum 70007922") == card_short


def test_get_date():
    assert get_date("2024-09-11T02:26:18.671407") == "11.09.2024"
    with pytest.raises(ValueError):
        get_date("T02:26:18.671407")
        get_date("2024-14-11T02:26:18.671407")
        get_date("2024-10-45T02:26:18.671407")
