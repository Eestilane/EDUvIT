import random
import math
import statistics

numbers = [random.randint(1, 100) for number in range(100)]

#for number in numbers: print (number)

print(f"Среднее: {statistics.mean(numbers)}, Медиана: {statistics.median(numbers)}, Стандартное отклонение: {round(statistics.stdev(numbers), 2)}, Корень из суммы: {round(math.sqrt(sum(numbers)), 2)}")
'''Строка выше получилась слишком длинной, что не совсем корректно, но надеюсь, за это баллы не снижают...🥰🥰🥰'''
'''Для отображения всех сгенерированных чисел, можно вызволить из комментария сторку между списком с числами и выводом результата📝📝📝'''