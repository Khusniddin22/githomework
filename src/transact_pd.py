import csv
import os

import pandas as pd

path_csv = os.path.join("..", "data", "transactions.csv")
path_excel = os.path.join("..", "data", "transactions_excel.xlsx")


def reading_transactions_csv(file_path_csv: str) -> list:
    """Считывает транзакции из CSV файла и возвращает список словарей"""
    try:
        transaction_list_csv = []
        with open(file_path_csv, "r", encoding="utf-8") as f_csv:
            if f_csv is None:
                return []
            else:
                reader = csv.DictReader(f_csv, delimiter=";")
                for row in reader:
                    transaction_list_csv.append(row)
                return transaction_list_csv
    except FileNotFoundError:
        return []


print(reading_transactions_csv(path_csv))


def reading_transactions_excel(file_path_excel: str) -> list:
    """Считывает транзакции из EXCEL файла и возвращает список словарей"""
    try:
        transactions_list_excel = []
        df_excel = pd.read_excel(file_path_excel)
        for index, row in df_excel.iterrows():
            dict_row = {
                "id": row["id"],
                "state": row["state"],
                "date": row["date"],
                "amount": row["amount"],
                "currency_name": row["currency_name"],
                "currency_code": row["currency_code"],
                "from": row["from"],
                "to": row["to"],
                "description": row["description"],
            }
            transactions_list_excel.append(dict_row)
        return transactions_list_excel
    except KeyError as ke:  # Добавляем обработку ошибки, если колонка не найдена
        print(f"Ошибка: Отсутствует колонка в Excel файле: {ke}")
        return []
    except Exception as e:  # Общая обработка других ошибок
        print(f"Произошла ошибка при чтении Excel файла: {e}")
        return []
