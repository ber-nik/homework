def filter_dicts_by_state(dicts_list: list, state: str = 'EXECUTED') -> list:
    return [d for d in dicts_list if d.get('state') == state]


