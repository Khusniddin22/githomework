from typing import Dict, List


def filter_by_state(list_of_dicts: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция возвращает отфильтрованный список словарей,
    у которых ключ state соответствует указанному значению"""
    filtered_list = []
    for dictionary in list_of_dicts:
        if state in dictionary.values():
            filtered_list.append(dictionary)
    return filtered_list


def sort_by_date(list_of_dicts: List[Dict], decreasing: bool = True) -> List[Dict]:
    """Функция возвращает отсортированный список по заданной дате"""
    sorted_list = sorted(list_of_dicts, key=lambda x: x["date"], reverse=decreasing)
    return sorted_list
