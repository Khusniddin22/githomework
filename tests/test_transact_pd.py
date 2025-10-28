from unittest.mock import patch
import os

from src.transact_pd import reading_transactions_csv
from src.transact_pd import reading_transactions_excel

path_csv = os.path.join('..', 'data', 'transactions.csv')

# Тест к функции reading_transactions_csv
@patch('src.transact_pd.csv.DictReader')
def test_reading_transactions_csv(mock_DictReader):
    mock_DictReader.return_value = [
        {
             'id': 650703,
             'state': 'EXECUTED',
             'date': '2023-09-05T11:30:32Z',
             'amount': 16210,
             'currency_name': 'Sol',
             'currency_code': 'PEN',
             'from': 'Счет 58803664561298323391',
             'to': 'Счет 39745660563456619397',
             'description': 'Перевод организации'
         },
        {
            'id': 3598919,
            'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58Z',
            'amount': 29740,
            'currency_name': 'Peso',
            'currency_code': 'COP',
            'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643',
            'description': 'Перевод с карты на карту'
        }
    ]
    result = reading_transactions_csv(path_csv)
    assert result == [
        {
             'id': 650703,
             'state': 'EXECUTED',
             'date': '2023-09-05T11:30:32Z',
             'amount': 16210,
             'currency_name': 'Sol',
             'currency_code': 'PEN',
             'from': 'Счет 58803664561298323391',
             'to': 'Счет 39745660563456619397',
             'description': 'Перевод организации'
         },
        {
            'id': 3598919,
            'state': 'EXECUTED',
            'date': '2020-12-06T23:00:58Z',
            'amount': 29740,
            'currency_name': 'Peso',
            'currency_code': 'COP',
            'from': 'Discover 3172601889670065',
            'to': 'Discover 0720428384694643',
            'description': 'Перевод с карты на карту'
        }
    ]
    mock_DictReader.assert_called_once()
