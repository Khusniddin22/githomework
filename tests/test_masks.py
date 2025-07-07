import pytest

from src.masks import get_mask_account, get_mask_card_number

def test_get_mask_card_number():
    assert get_mask_account(73654108430135874305) == '**4305'
    assert get_mask_account(73654108430135874.305) == None
    assert get_mask_account(7365410) == None


def
