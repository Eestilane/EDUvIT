import random
import json
import string

first_names = ["Artyom", "Andrey", "Afanasiy", "Amil", "Anton", "Grib"]
last_names = ["Artyomov", "Anrdreev", "Afanasiev", "Uzbekov", "Antonov", "Moooohomorov"]
full_name = f"{random.choice(first_names)} {random.choice(last_names)}"

def user():
    return {
        "name": full_name,
        "age": random.randint(14, 88),
        "email": f"{full_name.split()[0].lower()}.{full_name.split()[1].lower()}@mail.ru",
        "password": ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(12))
    }

with open('user.json', 'w') as file:
    json.dump(user(), file, indent=4)

with open('user.json', 'r') as file:
    print(file.read())
'''Мы живём в России, поэтому, можно использовать только почту с доменом @mail.ru🐘🐘🐘'''
'''Есть шанс (1 к 36) получить особого пользователя🍄‍🟫🍄‍🟫🍄‍🟫'''