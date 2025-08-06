import requests


def convert_currency(transaction: dict) -> float:
    API_KEY = 'SRFm93FO9ZIvG7A7jQG2s66u4nz5Y7QB'
    amount = transaction['operationAmount']['amount']
    code_currency = transaction['operationAmount']['currency']['code']
    rub = 'RUB'
    if code_currency not in ['USD', 'EUR']:
        return amount
    else:
        headers = {
            'apikey': 'SRFm93FO9ZIvG7A7jQG2s66u4nz5Y7QB'
        }
        url = f'https://api.apilayer.com/exchangerates_data/convert?to={rub}&from={code_currency}&amount={amount}'
        response = requests.get(url, headers=headers)
        result = response.json()['result']
        return result

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
        "amount": "8221.37",
        "currency": {
            "name": "USD",
            "code": "USD"
        }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}

print(convert_currency(transaction))
