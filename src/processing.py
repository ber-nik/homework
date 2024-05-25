def filter_by_state(dicts_list: list, state: str = "EXECUTED") -> list:
    """Функция принимает на вход список словарей и значение для ключа state
     (опциональный параметр со значением по умолчанию EXECUTED) и возвращает новый список,
    содержащий только те словари, у которых ключ state содержит переданное в функцию значение."""
    filtred_dict = []
    for i in dicts_list:
        if i.get("state") == state:
            filtred_dict.append(i)
    return filtred_dict


def sorted_by_date(dicst_list: list, direction: bool = True) -> list:
    """Функция принимает на вход список словарей и возвращает новый список, в котором исходные словари
    отсортированы по убыванию даты (ключ date)."""
    sorted_dicts = sorted(dicst_list, key=lambda x: x["date"], reverse=direction)
    return sorted_dicts
