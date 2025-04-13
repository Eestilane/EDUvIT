def task():
    number = 2
    while True:
        number_is_prime = True
        for dividers in range(2, int(number ** 0.5) + 1):
            if number % dividers == 0:
                number_is_prime = False
                break
        if number_is_prime:
            yield number
        number += 1

task = task()
for numbers in range(10):
    print(next(task))

'''Тут растут грибы  -> 🍄‍🟫🍄‍🟫🍄‍🟫'''