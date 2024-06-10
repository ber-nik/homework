import json
from json import JSONDecodeError


def get_jcon_transactions(file_path: str) -> list[dict] or []:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return json.loads(file.read())
    except JSONDecodeError:
        return []


if __name__ == "__main__":
    file_path = r"C:\Users\ЗС\work\tmp\homework\data\operations.json"
    transactions = get_jcon_transactions(file_path)
    print(transactions)
