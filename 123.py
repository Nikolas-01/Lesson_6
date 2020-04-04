# 1. проверка числа на простоту.
from math import sqrt
def num_simple(n):
    if n <= 1:
        return False
    i = 2
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True
n = int(input('Введите натуральное число '))
print('1) проверяем на простоту\n', num_simple(n))
5
def num_divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result
print('2) Вывод списка делителей числа\n', num_divisors(n))
def num_max_divisor(n):
    if n == 1:
        return None
    return max(list(filter(num_simple, num_divisors(n))))
print('3) Вывод самого большого простого делителя числа\n', num_max_divisor(n))

import unittest
class TestPrimeNum(unittest.TestCase):
    def num_simple(n):
        self.assertTrue(prime_num(101))

        def num_max_divisor(n):
        self.assertFalse (prime_num(102))


class TestGetDivisors(unittest.TestCase):
    def test_simple_3(self):
        self.assertEqual(get_divisors(50), [1, 2, 5, 10, 25, 50])


class TestGetMaxPrime(unittest.TestCase):
    def test_simple_1(self):
        self.assertEqual(get_max_prime(37), 37)

    def test_simple_2(self):
        self.assertNotEqual(get_max_prime(997), 996)

