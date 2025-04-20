import random
from datetime import datetime, timedelta
from array import array

dates = []

def random_date():
    return ((start_date := datetime.today() - timedelta(days=5*365)) + timedelta(days=random.randint(0, (datetime.today() - start_date).days))).date()

for date in range(10):
    dates.append(random_date())
    array('u', []).frombytes(random_date().isoformat().encode('utf-16-le'))

for date in range(9):
    print(f"Разница между {dates[date]} и {dates[date+1]}: {abs((dates[date+1] - dates[date]).days)} дней")
'''Мне попались рядом друг с другом только два соседних дня, но есть шанс, что в списке два раза подряд будет идти один и тот же день🎉🎉🎉'''