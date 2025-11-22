import os

from src.transact_pd import reading_transactions_csv, reading_transactions_excel
from src.widget import get_date, mask_account_card

path_json_file = os.path.join('data', 'operations.json')
path_to_csv = os.path.join("data", "transactions.csv")
path_to_excel = os.path.join("data", "transactions_excel.xlsx")

def main():
    print(f'''
    Привет! Добро пожаловать в программу работы с банковскими транзакциями. 
    Выберите необходимый пункт меню:
    1. Получить информацию о транзакциях из JSON-файла
    2. Получить информацию о транзакциях из CSV-файла
    3. Получить информацию о транзакциях из XLSX-файла''')

    user_select_file = int(input())

    # Работа с JSON-файлом
    if user_select_file == 1:
        print('Для обработки выбран JSON-файл')
        print('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')

        df_csv = reading_transactions_csv(path_json_file)
        df_state_json = []
        while True:
            user_select_filter = input().upper()
            if user_select_filter in ('EXECUTED', 'CANCELED', 'PENDING'):
                if user_select_filter == 'EXECUTED':
                    for transaction in df_csv:
                        if transaction['state'] == 'EXECUTED':
                            df_state_json.append(transaction)
                elif user_select_filter == 'CANCELED':
                    for transaction in df_csv:
                        if transaction['state'] == 'CANCELED':
                            df_state_json.append(transaction)
                else:
                    for transaction in df_csv:
                        if transaction['state'] == 'PENDING':
                            df_state_json.append(transaction)
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_select_filter}'. Пожалуйста, введите один из следующих: {('EXECUTED', 'CANCELED', 'PENDING')}")

        print('Отсортировать операции по дате? Да/Нет')
        user_input = input().upper()
        if user_input == 'ДА':
            df_state_json = sorted(df_state_json, key=lambda x: x['date'])
        else:
            pass

        print('Отсортировать по возрастанию или по убыванию?')
        while True:
            user_input = input().lower()
            if user_input in ('по возрастанию', 'по убыванию'):
                if user_input == 'по возрастанию':
                    df_state_json = sorted(df_state_json, key=lambda x: x['id'], reverse=False)
                else:
                    df_state_json = sorted(df_state_json, key=lambda x: x['id'], reverse=True)
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('по возрастанию', 'по убыванию')}")

        print('Выводить только рублевые транзакции? Да/Нет')
        while True:
            user_input = input()
            if user_input in ('Да', 'Нет'):
                if user_input == 'Да':
                    df_state_json = [
                        transaction for transaction in df_state_json
                        if transaction['currency_code'] == 'RUB'
                    ]
                else:
                    pass
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('Да', 'Нет')}")

        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        while True:
            user_input = input()
            if user_input in ('Да', 'Нет'):
                if user_input == 'Да':
                    df_state_json = sorted(df_state_json, key=lambda x: x['description'])
                else:
                    pass
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('Да', 'Нет')}")

        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(df_state_json)}')
        for transaction in df_state_json:
            transaction['date'] = get_date(transaction['date'])
            if transaction['from'] != '':
                transaction['from'] = mask_account_card(transaction['from'])
            transaction['to'] = mask_account_card(transaction['to'])

        for transaction in df_state_json:
            print(transaction['date'], transaction['description'])
            if transaction['from'] != '':
                print(transaction['from'] + ' -> ' + transaction['to'])
                print(f'Сумма: {transaction['amount']} {transaction['currency_code']}\n')
            else:
                print(transaction['to'])
                print(f'Сумма: {transaction['amount']} {transaction['currency_code']}\n')
        if df_state_json == []:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

    # Работа с CSV-файлом
    elif user_select_file == 2:
        print('Для обработки выбран CSV-файл')
        print('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        df_csv = reading_transactions_csv(path_to_csv)
        df_state_csv = []
        while True:
            user_select_filter = input().upper()
            if user_select_filter in ('EXECUTED', 'CANCELED', 'PENDING'):
                if user_select_filter == 'EXECUTED':
                    for transaction in df_csv:
                        if transaction['state']=='EXECUTED':
                            df_state_csv.append(transaction)
                elif user_select_filter == 'CANCELED':
                    for transaction in df_csv:
                        if transaction['state']=='CANCELED':
                            df_state_csv.append(transaction)
                else:
                    for transaction in df_csv:
                        if transaction['state']=='PENDING':
                            df_state_csv.append(transaction)
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_select_filter}'. Пожалуйста, введите один из следующих: {('EXECUTED', 'CANCELED', 'PENDING')}")

        print('Отсортировать операции по дате? Да/Нет')
        user_input = input().upper()
        if user_input == 'ДА':
            df_state_csv = sorted(df_state_csv, key=lambda x: x['date'])
        else:
            pass

        print('Отсортировать по возрастанию или по убыванию?')
        while True:
            user_input = input().lower()
            if user_input in ('по возрастанию', 'по убыванию'):
                if user_input == 'по возрастанию':
                    df_state_csv = sorted(df_state_csv, key=lambda x: x['id'], reverse=False)
                else:
                    df_state_csv = sorted(df_state_csv, key=lambda x: x['id'], reverse=True)
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('по возрастанию', 'по убыванию')}")

        print('Выводить только рублевые транзакции? Да/Нет')
        while True:
            user_input = input()
            if user_input in ('Да', 'Нет'):
                if user_input == 'Да':
                    df_state_csv = [
                        transaction for transaction in df_state_csv
                        if transaction['currency_code'] == 'RUB'
                    ]
                else:
                    pass
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('Да', 'Нет')}")

        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        while True:
            user_input = input()
            if user_input in ('Да', 'Нет'):
                if user_input == 'Да':
                    df_state_csv = sorted(df_state_csv, key=lambda x: x['description'])
                else:
                    pass
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('Да', 'Нет')}")

        for transaction in df_state_csv:
            transaction['date'] = get_date(transaction['date'])
            if transaction['from'] != '':
                transaction['from'] = mask_account_card(transaction['from'])
            transaction['to'] = mask_account_card(transaction['to'])

        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(df_state_csv)}')

        for transaction in df_state_csv:
            print(transaction['date'], transaction['description'])
            if transaction['from'] != '':
                print(transaction['from'] + ' -> ' + transaction['to'])
                print(f'Сумма: {transaction['amount']} {transaction['currency_code']}\n')
            else:
                print(transaction['to'])
                print(f'Сумма: {transaction['amount']} {transaction['currency_code']}\n')

        if df_state_csv == []:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

    # Работа с Excel-файлом
    else:
        print('Для обработки выбран XLSX-файл')
        print('Введите статус, по которому необходимо выполнить фильтрацию.\nДоступные для фильтровки статусы: EXECUTED, CANCELED, PENDING')
        df_excel = reading_transactions_excel(path_to_excel)
        df_state_excel = []
        while True:
            user_select_filter = input().upper()
            if user_select_filter in ('EXECUTED', 'CANCELED', 'PENDING'):
                if user_select_filter == 'EXECUTED':
                    for transaction in df_excel:
                        if transaction['state'] == 'EXECUTED':
                            df_state_excel.append(transaction)
                elif user_select_filter == 'CANCELED':
                    for transaction in df_excel:
                        if transaction['state'] == 'CANCELED':
                            df_state_excel.append(transaction)
                else:
                    for transaction in df_excel:
                        if transaction['state'] == 'PENDING':
                            df_state_excel.append(transaction)
                break
            else:
                print(f"Ошибка: Некорректный статус '{user_select_filter}'. Пожалуйста, введите один из следующих: {('EXECUTED', 'CANCELED', 'PENDING')}")

        print('Отсортировать операции по дате? Да/Нет')
        user_input = input().upper()
        if user_input == 'ДА':
            df_state_excel = sorted(df_state_excel, key=lambda x: x['date'])
        else:
            pass

        print('Отсортировать по возрастанию или по убыванию?')
        while True:
            user_input = input().lower()
            if user_input in ('по возрастанию', 'по убыванию'):
                if user_input == 'по возрастанию':
                    df_state_excel = sorted(df_state_excel, key=lambda x: x['id'], reverse=False)
                else:
                    df_state_excel = sorted(df_state_excel, key=lambda x: x['id'], reverse=True)
                break
            else:
                print(
                    f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('по возрастанию', 'по убыванию')}")

        print('Выводить только рублевые транзакции? Да/Нет')
        while True:
            user_input = input()
            if user_input in ('Да', 'Нет'):
                if user_input == 'Да':
                    df_state_excel = [
                        transaction for transaction in df_state_excel
                        if transaction['currency_code'] == 'RUB'
                    ]
                else:
                    pass
                break
            else:
                print(
                    f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('Да', 'Нет')}")

        print('Отфильтровать список транзакций по определенному слову в описании? Да/Нет')
        while True:
            user_input = input()
            if user_input in ('Да', 'Нет'):
                if user_input == 'Да':
                    df_state_excel = sorted(df_state_excel, key=lambda x: x['description'])
                else:
                    pass
                break
            else:
                print(
                    f"Ошибка: Некорректный статус '{user_input}'. Пожалуйста, введите один из следующих: {('Да', 'Нет')}")

        for transaction in df_state_excel:
            transaction['date'] = get_date(transaction['date'])
            if transaction['from'] != '':
                transaction['from'] = mask_account_card(transaction['from'])
            transaction['to'] = mask_account_card(transaction['to'])

        print('Распечатываю итоговый список транзакций...')
        print(f'Всего банковских операций в выборке: {len(df_state_excel)}')
        for transaction in df_state_excel:
            print(transaction['date'], transaction['description'])
            if transaction['from'] != '':
                print(transaction['from'] + ' -> ' + transaction['to'])
                print(f'Сумма: {transaction['amount']} {transaction['currency_code']}\n')
            else:
                print(transaction['to'])
                print(f'Сумма: {transaction['amount']} {transaction['currency_code']}\n')
        if df_state_excel == []:
            print('Не найдено ни одной транзакции, подходящей под ваши условия фильтрации')

main()