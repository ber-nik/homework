def filter_by_state(dicts_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает на вход список словарей и значение для ключа state
     (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение."""
    return [d for d in dicts_list if d.get("state") == state]

def sorted_by_date(dicst_list: list) -> list:
    """Функция принимает на вход список словарей и возвращает новый список, в котором исходные словари
    отсортированы по убыванию даты (ключ date)."""
    sorted_dicts = sorted(dicst_list, key=lambda x: x['date'], reverse=True)
    return sorted_dicts

