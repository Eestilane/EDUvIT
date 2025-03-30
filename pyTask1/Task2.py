def task():
    number = input("Введите число: ")
    
    try:
        number = int(number)

        if number < 0:
            print("Ошибка: введно отрицательное число")
        elif number % 2 == 0:
            print(f"Число {number} является чётным")
        elif number % 2 != 0:
            print(f"Число {number} не является чётным")

    except ValueError:
        print("Ошибка: введено не число")
        
task()
