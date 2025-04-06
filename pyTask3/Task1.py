from typing import List, TypeVar, Union

T = TypeVar('T', int, float, str)

def get_multiplier(prompt: str) -> Union[int, float]:
    while True:
        multiplier = input(prompt)
        if not multiplier:
            return 2
        try:
            return float(multiplier) if '.' in multiplier else int(multiplier)
        except:
            print("Введите корректное значение")

def func(elements: List[T], multiplier: Union[int, float] = 2) -> List[T]:
    return [element * multiplier for element in elements]

def lambda_func(elements: List[T], multiplier: Union[int, float] = 2) -> List[T]:
    return list(map(lambda element: element * multiplier, elements))

def task():
    input_list = input("Введите список чисел через пробел: ").split()
    try:
        numbers = [int(num) for num in input_list]
    except:
        try:
            numbers = [float(num) for num in input_list]
        except:
            numbers = input_list

    multiplier = get_multiplier("Введите множитель (по умолчанию 2): ")

    result_func = func(numbers, multiplier)
    result_lambda = lambda_func(numbers, multiplier)

    print(f"Результат (функция): {result_func}")
    print(f"Результат (лямбда-функция): {result_lambda}")

task()