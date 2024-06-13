import logging

logger = logging.getLogger("masks")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/ masks.log")
file_formater = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formater)
logger.addHandler(file_handler)


def mask_card_number(card: str) -> str:
    """функция принимает номер карты и возвращает его зашифрованным"""
    masked_number = f"{card[:4]} {card[4:6]}** **** {card[-4:]}"

    logger.info(f"Получаем зашифрованный номер карты {masked_number}")
    return masked_number


def mask_account_number(account: str) -> str:
    """функция принимает номер счета и возвращает его зашифрованным"""
    masked_acc = f"**{account[-4:]}"
    return masked_acc
