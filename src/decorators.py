from functools import wraps


def log(filename=None):
    def my_decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            try:
                result = func(*args, **kwargs)
                log_message = f'{func.__name__} ok'
                if filename == None:
                    print(log_message)
                else:
                    with open(filename, 'a') as file_log:
                        file_log.write(log_message)
                return result
            except ValueError:
                error_message = f'{func.__name__}: Неправильно ввели данные. Input: ({args})'
                if filename == None:
                    print(error_message)
                else:
                    with open(filename, 'a') as file_log:
                        file_log.write(error_message)
                return None
            except ZeroDivisionError:
                error_message = f'{func.__name__}: На ноль делить нельзя!. Input: ({args})'
                if filename == None:
                    print(error_message)
                else:
                    with open(filename, 'a') as file_log:
                        file_log.write(error_message)
                return None
        return wrapper
    return my_decorator

@log()
def my_function(x, y):
    return x / y

my_function(1, 0)