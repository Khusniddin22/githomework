import os
from dotenv import load_dotenv
import requests

load_dotenv('.env')

def convert_currency(transaction: dict) -> float:
    amount = transaction['operationAmount']['amount']
    code_currency = transaction['operationAmount']['currency']['code']
    rub = 'RUB'
    if code_currency not in ['USD', 'EUR']:
        return amount
    else:
        API_KEY = os.getenv('API_KEY')
        headers = {
            "apikey": API_KEY
        }
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={code_currency}&amount={amount}'
        response = requests.get(url, headers=headers)
        result = response.json()['result']
        return result

