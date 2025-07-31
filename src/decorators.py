from functools import wraps


def log(filename=None):
    """Функция, которая автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки."""
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """Обертка функции"""
            try:
                result = func(*args, **kwargs)
                # Если ф-ия выполнилась, то выводится 'ok'
                log_message = f'{func.__name__} ok'
                if filename == None:
                    print(log_message)
                else:
                    with open(filename, 'a') as file_log:
                        file_log.write(log_message)
                return result
            except Exception as e:
                # Вызывается исключение и тип ошибки с введенными аргументами
                error_message = f'{func.__name__}: {type(e).__name__}. Input: ({args})'
                if filename == None:
                    print(error_message)
                else:
                    with open(filename, 'a') as file_log:
                        file_log.write(error_message)
                return None
        return wrapper
    return my_decorator

