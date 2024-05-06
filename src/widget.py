from src.masks import mask_account_number, mask_card_number


def mask_account_card(number: str) -> str:
    """Функция принимает строку и маскирует номер карты или счета"""
    if len(number.split()[-1]) == 16:
        mask_card = mask_card_number(number.split()[-1])
        result = f"{number[:-16]}{mask_card}"
    elif len(number.split()[-1]) == 20:
        mask_account = mask_account_number(number.split()[-1])
        result = f"{number[: -20]}{mask_account}"

    return result


def get_date(date: str) -> str:
    """Функүиә принимает строку записи даты и форматирует ее"""
    date_list = date[0:10].split("-")
    new_date = ".".join(date_list[::-1])

    return new_date
