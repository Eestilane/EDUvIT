import random
from pathlib import Path

def files_creator(directory):
    Path(directory).mkdir(parents=True, exist_ok=True)
    
    files = []

    for _ in range(10):
        file_path = Path(directory) / (''.join(random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(8)) + '.txt')
        file_path.touch()
        files.append(file_path) 
    
    return files

for file in files_creator(r"C:\Users\Eestilane\Documents\Учёба\2 Курс\Лабораторные работы\Технологии обработки информации\pyTask5"):
    print(file.absolute())
'''В коде указан путь к папке с лабораторными работами, путь для проверки задания, явно, будет другой🥲🥲🥲'''