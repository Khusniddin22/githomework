import pytest
from src.decorators import log

def test_log_console_success(capsys):
    @log()
    def log_sum(x, y):
        return x + y

    result = log_sum(5, 5)
    captured = capsys.readouterr()
    assert captured.out == 'log_sum ok\n'


def test_log_console_exception(capsys):
    @log()
    def log_dev(x, y):
        return x / y

    result = log_dev(5, 0)
    captured = capsys.readouterr()
    assert captured.out == 'log_dev: ZeroDivisionError. Input: ((5, 0))\n'


def test_log_file_succes():
    @log('mylog.txt')
    def log_sub(x, y):
        return x - y

    result = log_sub(10, 5)
    assert result == 5
    with open('mylog.txt', 'r') as f:
        log_message = f.read()
        assert 'log_sub ok' in log_message


def test_log_file_exception():
    @log('mylog.txt')
    def log_dev(x, y):
        return x / y

    result = log_dev(10, 0)
    assert result == None
    with open('mylog.txt', 'r') as f:
        log_message = f.read()
        assert 'log_dev: ZeroDivisionError. Input: ((10, 0))' in log_message