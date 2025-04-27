import unittest
import sys

def factorial(n: int):
    if n < 0:
        raise ValueError("Факториал отрицательного числа не определен")
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
        if result > sys.maxsize:
            raise ValueError(f"Факториал для {n} не поддерживается типом int")
    return result

class TestFactorial(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(10), 3628800)

    def test_zero(self):
        self.assertEqual(factorial(0), 1)

    def test_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial(-3)
        with self.assertRaises(ValueError):
            factorial(-35)

    def test_no_int_numbers(self):
        with self.assertRaises(TypeError):
            factorial(2.17)  
        with self.assertRaises(TypeError):
            factorial("777")   

    def test_crush_test(self):
        number = 1
        result = 1
        while True:
            try:
                result *= number
                if result > sys.maxsize:
                    break
                number += 1
            except OverflowError:
                break
        with self.assertRaises(ValueError):
            factorial(number)

unittest.main()

'''Если первым словом в названии не стоит слово тест, тест запустить не получится, поэтому, существует "тест краш тест"'''