def task():
    number = input("Введите ваш возраст: ")

    try:
        number = int(number)

        if number < 0:
            print("Ошибка: возраст не может быть отрицательным!")
        elif number >= 18:
            print("Вы совершеннолетний.")
        elif number < 18:
            print("Вы несовершеннолетний.")

    except:
        print("Ошибка: введено не число!")

task()