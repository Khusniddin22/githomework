from mypy.state import state


def filter_by_state(list_of_dict: list[dict], state='EXECUTED')->list:
    """Функция возвращает отфильтрованный список словарей, у которых ключ state соответствует указанному значению"""
    filtered_list = []
    for dictionary in list_of_dict:
        for key in dictionary:
            if dictionary[key] == state:
                filtered_list.append(dictionary)
    return filtered_list

print(filter_by_state([{'id': 41428829, 'state': 'CANCELED', 'date': '2019-07-03T18:35:29.512364'}, {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]
, state='CANCELED'))