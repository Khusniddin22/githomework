from unittest.mock import patch

from src.external_api import convert_currency

transaction = {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {"amount": "8221.37", "currency": {"name": "USD", "code": "USD"}},
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560",
}


def test_convert_currency():
    with patch("src.external_api.requests.get") as mock_get:
        mock_get.return_value.json.return_value = {"result": 657684.212409}
        result = convert_currency(transaction)
        assert result == {"result": 657684.212409}["result"]
        headers = {"apikey": None}
        mock_get.assert_called_once_with(
            "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37", headers=headers
        )
