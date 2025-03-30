def task():
    while True:
        number = input("Введите число: → ")
        
        if number == "exit":
            print("Выход из программы...")
            break
        
        if number.lstrip('-').isdigit():
            length = len(number.lstrip('-'))
            print(f"В этом числе {length} цифры.\n")
        else:
            print("Ошибка: данные не являются числом.\n")

task()