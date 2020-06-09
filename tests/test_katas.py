import unittest
import katas


class TestKatas(unittest.TestCase):
    def test_add(self):
        result_from_add_kata = katas.add(2, 2)
        self.assertEqual(result_from_add_kata, 4)

    def test_multiply(self):
        result_from_multiply_kata = katas.multiply(9, 9)
        self.assertEqual(result_from_multiply_kata, 81)

    def test_power(self):
        result_from_power_kata = katas.power(2, 5)
        self.assertEqual(result_from_power_kata, 32)

    def test_factorial(self):
        result_from_factorial_kata = katas.factorial(4)
        self.assertEqual(result_from_factorial_kata, 24)

    def test_fibonacci(self):
        result_from_fibonacci_kata = katas.fibonacci(8)
        self.assertEqual(result_from_fibonacci_kata, 13)


if __name__ == '__main__':
    unittest.main()
