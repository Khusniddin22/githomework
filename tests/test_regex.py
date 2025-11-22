from collections import Counter

import pytest

from src.regex import process_bank_operations, process_bank_search


@pytest.fixture
def sample_transactions():
    """Возвращает список тестовых транзакций."""
    return [
        {"id": "650703", "state": "EXECUTED", "date": "2023-09-05T11:30:32Z", "description": "Перевод организации"},
        {"id": "3598919", "state": "EXECUTED", "date": "2020-12-06T23:00:58Z", "description": "Открытие вклада"},
        {"id": "593027", "state": "CANCELED", "date": "2023-07-22T05:02:01Z", "description": "Открытие вклада"},
        {"id": "4699552", "state": "EXECUTED", "date": "2022-03-23T08:29:37Z", "description": "Перевод организации"},
        {"id": "1234567", "state": "EXECUTED", "date": "2021-01-15T10:00:00Z", "description": "Покупка продуктов"},
        {"id": "7654321", "state": "CANCELED", "date": "2023-11-20T14:15:30Z", "description": "Оплата услуг"},
    ]


# Тесты к функции process_bank_search
def test_process_bank_search_not_found(sample_transactions):
    """Тест на случай, когда транзакции не найдены."""
    search_string = "Несуществующий_поиск"
    found = process_bank_search(sample_transactions, search_string)
    assert len(found) == 0
    assert found == []


def test_process_bank_search_case(sample_transactions):
    """Тест на IGNORECASE"""
    search_string = "перевод"
    found = process_bank_search(sample_transactions, search_string)
    assert found == []  # Без re.IGNORECASE это будет 0


def test_process_bank_search_partial_match(sample_transactions):
    """Тест на поиск части слова"""
    search_string = "орган"
    found = process_bank_search(sample_transactions, search_string)
    assert len(found) == 2
    assert "Перевод организации" in found[0]["description"]
    assert "Перевод организации" in found[1]["description"]


# Тесты к функции process_bank_operations
def test_process_bank_operations_correctly(sample_transactions):
    """Тест на корректный подсчет по категориям"""
    categories_to_count = ["Перевод организации", "Открытие вклада", "Покупка продуктов"]
    counts = process_bank_operations(sample_transactions, categories_to_count)
    expected_counts = Counter({"Перевод организации": 2, "Открытие вклада": 2, "Покупка продуктов": 1})
    assert counts == expected_counts


def test_process_bank_operations_no_matching_categories(sample_transactions):
    """Тест на случай, когда нет совпадающих категорий"""
    categories_to_count = ["Неизвестная операция", "Продажа недвижимости"]
    counts = process_bank_operations(sample_transactions, categories_to_count)
    assert counts == Counter()


def test_process_bank_operations_empty_list_of_categories(sample_transactions):
    """Тест на пустой список категорий"""
    categories_to_count = []
    counts = process_bank_operations(sample_transactions, categories_to_count)
    assert counts == Counter()
