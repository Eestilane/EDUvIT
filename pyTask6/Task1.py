def average_num(list_num: list) -> float:
    for ind, el in enumerate(list_num):
        if not isinstance(el, int | float):
            try:
                list_num[ind] = int(el)
            except:
                return "Bad request"
    return round(sum(list_num) / len(list_num), 2)

assert average_num([1, 2, 3, 4, 5]) == 3.0

assert average_num([1.5, 2.5, 3.5]) == 2.5

assert average_num([1, 2.5, 3, 4.5]) == 2.75

assert average_num([777]) == 777.0

assert average_num([11, 12, 13, 14]) == 12.5

assert average_num([0, 0]) == 0.0

assert average_num([10000, 20000, 30000]) == 20000.0

assert average_num(["6", "7", "8"]) == 7.0

assert average_num(["z", "o", "v"]) == "Bad request"

try:
    average_num([])
    assert False, "Ошибка выполнения, пустой список"
except:
    pass

print("Все тесты пройдены")