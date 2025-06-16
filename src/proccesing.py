from src.widget import get_date
from typing import List, Dict
def filter_by_state(list_of_dict: List[Dict], state='EXECUTED')->List[Dict]:
    """Функция возвращает отфильтрованный список словарей, у которых ключ state соответствует указанному значению"""
    filtered_list = []
    for dictionary in list_of_dict:
        for key in dictionary:
            if dictionary[key] == state:
                filtered_list.append(dictionary)
    return filtered_list


def sort_by_date(list_of_dict: List[Dict], desc=True)->List[Dict]:
    """Функция возвращает отсортированный список по заданной дате"""
    sorted_list = sorted(list_of_dict, key=lambda x: x['date'], reverse=desc)
    return sorted_list

