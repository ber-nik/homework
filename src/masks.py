def mask_card_number(card: str) -> str:
    """функция принимает номер карты и возвращает его зашифрованным"""
    masked_number = f"{card[:4]} {card[4:6]}** **** {card[-4:]}"
    return masked_number


def mask_account_number(account: str) -> str:
    """функция принимает номер счета и возвращает его зашифрованным"""
    masked_number = f"**{account[-4:]}"
    return masked_number
