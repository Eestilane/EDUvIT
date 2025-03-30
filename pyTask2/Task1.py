def task():
    numbers = input("Введите числа через пробел: ").split()
    power = int(input("Введите степень: "))
    result = []

    for number in numbers:
        try:
            number = float(number)
            if number.is_integer():
                number = int(number)
            result.append(str(number ** power))
        except:
            result.append(number * power)

    print("Вывод:", " ".join(result))

task()