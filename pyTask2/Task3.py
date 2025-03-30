def task():
    list1 = input("Введите первый список: ").split()
    list2 = input("Введите второй список: ").split()

    elements = set(list1).intersection(set(list2))

    print("Общие элементы:", " ".join(elements))

task()