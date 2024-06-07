import json
import os

def get_jcon_transactions(file_path: list[dict]) -> list[dict] or []:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            return json.loads(f.read())
    except:
        return []

file_path = r'C:\Users\ЗС\work\tmp\homework\data\operations.json'
transactions = get_jcon_transactions(file_path)
print(transactions)
