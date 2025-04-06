import math

def calculator():
    while True:
        print("Доступные операции:")
        print("1. Сложение")
        print("2. Вычитание")
        print("3. Умножение")
        print("4. Деление")
        print("5. Возведение в степень")
        print("6. Факториал")
        print("7. Логарифм")
        print("8. Квадратный корень")
        print("'exit' для выхода")
        print("--------------------")
        
        operation = input("Операция: ")
        
        match operation:
            case "1":
                addition()
            case "2":
                subtraction()
            case "3":
                multiplication()
            case "4":
                division()
            case "5":
                exponentiation()
            case "6":
                factorial()
            case "7":
                logarithm()
            case "8":
                square_root()
            case "exit":
                print("Выход из калькулятора")
                print("--------------------")
                break
            case _:
                print("Такой операции не существует!")
                print("--------------------")
                continue
        
        print("--------------------")

def get_number(text):
    while True:
        try:
            number = input(text)
            return float(number) if '.' in number else int(number)
        except:
            print("Введите число")

def addition():
    number1 = get_number("Слагаемое 1: ")
    number2 = get_number("Слагаемое 2: ")

    if not all(isinstance(number, (int, float)) for number in (number1, number2)):
        raise TypeError("Некорректные аргументы")
    
    print(f">>> {number1 + number2}")

def subtraction():
    number1 = get_number("Уменьшаемое: ")
    number2 = get_number("Вычитаемое: ")

    if not all(isinstance(number, (int, float)) for number in (number1, number2)):
        raise TypeError("Некорректные аргументы")
    
    print(f">>> {number1 - number2}")

def multiplication():
    number1 = get_number("Множитель 1: ")
    number2 = get_number("Множитель 2: ")

    if not all(isinstance(number, (int, float)) for number in (number1, number2)):
        raise TypeError("Некорректные аргументы")
    
    print(f">>> {number1 * number2}")

def division():
    print("Доступные типы деления:")
    print("1. Обычное деление")
    print("2. Целочисленное деление")
    print("3. Остаток от деления")
    
    choice = input("Тип деления: ")

    if choice not in ("1", "2", "3"):
        raise ValueError("Неверный выбор операции деления")
    
    number1 = get_number("Делимое: ")
    number2 = get_number("Делитель: ")
    
    if not all(isinstance(number, (int, float)) for number in (number1, number2)):
        raise TypeError("Некорректные аргументы")
    
    if number2 == 0:
        raise ZeroDivisionError("Нельзя делить на 0")
    
    match choice:
        case "1":
            print(f">>> {number1 / number2}")
        case "2":
            print(f">>> {number1 // number2}")
        case "3":
            print(f">>> {number1 % number2}")
        case _:
            print("Такой вариант недоступен")

def exponentiation():
    number1 = get_number("Основание: ")
    number2 = get_number("Степень: ")
    if not all(isinstance(number, (int, float)) for number in (number1, number2)):
        raise TypeError("Некорректные аргументы")
    print(f">>> {number1 ** number2}")

def factorial():
    number = get_number("Число: ")
    if not isinstance(number, int):
        raise TypeError("Факториал вычисляется только для целых чисел")
    if number < 0:
        raise ValueError("Нельзя вычислить факториал для отрицательных чисел")
    print(f">>> {math.factorial(number)}")

def logarithm():
    number1 = get_number("Число: ")
    number2 = get_number("Основание логарифма: ")
    
    if not all(isinstance(number, (int, float)) for number in (number1, number2)):
        raise TypeError("Оба аргумента должны быть числами")
    
    if number1 <= 0:
        raise ValueError("Число должно быть положительным")
    if number2 <= 0 or number2 == 1:
        raise ValueError("Основание должно быть положительным и не равным 1")
    
    print(f">>> {math.log(number1, number2)}")

def square_root():
    number = get_number("Число: ")
    if not isinstance(number, (int, float)):
        raise TypeError("Некорректный аргумент")
    if number < 0:
        raise ValueError("Нельзя взять корень из отрицательного числа")
    print(f">>> {math.sqrt(number)}")

calculator()