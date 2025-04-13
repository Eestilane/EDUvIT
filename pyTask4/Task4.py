def decorator(function):
    def function_in_decorator(*args, **kwargs):
        print(f"Функция {function.__name__} вызвана с аргументами:")
        print(f"Позиционные аргументы: {args}")
        print(f"Именованные аргументы: {kwargs}")
        print(f"Площадь прямоугольника: {function(*args, **kwargs)}")
        return function(*args, **kwargs)
    return function_in_decorator

@decorator
def calculate_area(length, width):
    return length * width

calculate_area(13, 37)
print()
calculate_area(length = 13, width = 37)
'''Первый вызов функции использует позиционные аргументы, а второй именованные 🎉🎉🎉'''