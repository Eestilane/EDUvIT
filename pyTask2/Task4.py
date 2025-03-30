def task():
    text = input("Введите строку: ").lower().split()
    dct = {}

    for word in text:
        if word in dct:
           dct[word] += 1
        else:
            dct[word] = 1

    for word in dct:
      print(f"{word}: {dct[word]}")

task()