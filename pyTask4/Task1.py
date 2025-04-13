from math import factorial

def task():
    list_of_days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    list_of_libraries = ["Django", "FastAPI", "Numpy", "PYTHON", "Pandas", "FASTAPI", "Python", "random"]

    #1
    print([number ** 2 for number in range(1, 11)])

    #2
    print({day: number + 1 for number, day in enumerate(list_of_days)})

    #3
    print([lib.lower() for lib in list_of_libraries if not (lib in set() or set().add(lib))])

    #4
    print([number for number in [1, 3, 4, 87, 98, 15, 7, 4] if number % 2 == 0])

    #5
    print({number: factorial(number) for number in range(1, 6)})

task()
'''В 3 задании почему-то используется .lower(), хотя библиотеки даны с явным учётом регистра'''