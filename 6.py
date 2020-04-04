# Проверка числа на простоту
import unittest
def prime_num(n):
    if n == 1:
        return False
    for i in range(2, n + 1):
        if n % i == 0 and i == n:
            return True
        elif n % i == 0 and i != n:
            return False
# список всех делителей числа
def get_divisors(n):
    lst_divisors = []
    for i in range(1, n + 1):
        if n % i == 0:
            lst_divisors.append(i)
    return lst_divisors
#самый большой простой делитель числа
def get_max_prime(n):
    lst_max_prime = []
    lst_divs = get_divisors(n)
    for i in lst_divs:
        if prime_num(i):
            lst_max_prime.append(i)
    return max(lst_max_prime)
class TestPrimeNum(unittest.TestCase):
    def test_simple_1(self):
        self.assertTrue(prime_num(101))
    def test_simple_2(self):
        self.assertFalse(prime_num(102))
class TestGetDivisors(unittest.TestCase):
    def test_simple_3(self):
        self.assertEqual(get_divisors(50), [1, 2, 5, 10, 25, 50])
class TestGetMaxPrime(unittest.TestCase):
    def test_simple_1(self):
        self.assertEqual(get_max_prime(37), 37)
    def test_simple_2(self):
        self.assertNotEqual(get_max_prime(997), 996)
class TestPrimeNum(unittest.TestCase):
    def test_simple_1(self):
        self.assertTrue(prime_num(101))
    def test_simple_2(self):
        self.assertFalse(prime_num(102))
import unittest
class TestGetDivisors(unittest.TestCase):
    def test_simple_3(self):
        self.assertEqual(get_divisors(50), [1, 2, 5, 10, 25, 50])
class TestGetMaxPrime(unittest.TestCase):
    def test_simple_1(self):
        self.assertEqual(get_max_prime(37), 37)
    def test_simple_2(self):
        self.assertNotEqual(get_max_prime(997), 996)
