def task():
    dct = {1: 11, 2: 22, 3: 33, 4: 4, 5: 33, 6: 1}

    print("Множество ключей:", set(dct.keys()))
    print("Множество значений:", set(dct.values()))
    print("Объединение множеств:", set(dct.keys()) | set(dct.values()))

task()