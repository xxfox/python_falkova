





"""
Написать декоратор с аргументом-функцией (callback), позволяющий валидировать входные
значения функции и выбрасывать исключение ValueError, если что-то не так
"""
def val_checker(condition):
    def _val_checker(func):
        def wrapper(*args, **kwargs):
            for item in args:
                if condition(item):
                    return func(*args, **kwargs)
                else:
                    raise ValueError('Wrong value, please try again')
        return wrapper
    return _val_checker


@val_checker(lambda x: x > 0)
def calc_cube(*args):
    for item in args:
        print(item ** 3)


calc_cube(5)
calc_cube(-5)




