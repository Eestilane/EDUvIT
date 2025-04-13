def append_to_file(text, filename):
    with open(filename, 'a', encoding = 'utf-8') as file:
        file.write(text + '\n')
    
    with open(filename, 'r', encoding = 'utf-8') as file:
        print('\n'.join([string.strip() for number_of_string, string in enumerate(file.readlines(), 1) if number_of_string % 2 == 0]))

# append_to_file("Первая строка", "example.txt")
# append_to_file("Вторая строка", "example.txt")
# append_to_file("Третья строка", "example.txt")
# append_to_file("Четвертая строка", "example.txt")

append_to_file("Пятая строка", "example.txt")
'''Файл уже создан и отредактирован при помощи первых 4 вызовов функции, он должен лежать в папке с заданием - pyTask4,
   при запуске кода должен получиться результат, подобный указанному в примере 🎅🏿🎅🏿🎅🏿'''