import re

def palindrome(text: str) -> bool:
    text = re.sub(r'[^a-zа-яё0-9]', '', text.lower())
    return text == text[::-1]

assert palindrome("Шалаш") == True

assert palindrome("У лип Леша нашел пилу") == True

assert palindrome("Привет, мир!") == False

assert palindrome("12321") == True

assert palindrome("") == True

assert palindrome("Madam, I’m Adam") == True

assert palindrome("Аргентина манит негра!") == True

print("Все тесты пройдены")

'''Обрабатывает текст со знаками препинания'''