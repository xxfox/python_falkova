"""
Написать декоратор для выведения типов позиционных аргументов функции
"""
def type_logger(func):
    def wrapper(*args, **kwargs):
        elements = args
        for el in elements:
            print(type(el))
        return func(*args, **kwargs)
    return wrapper


@type_logger
def calc_cube(*args):
    for item in args:
        print(item ** 3)


calc_cube(2, 10.5, 4)