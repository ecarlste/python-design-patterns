import unittest

from decorator.adder import adder
from decorator.multiplier import multiplier


class DecoratorTest(unittest.TestCase):
    def test_returns_1_should_return_1(self):
        self.assertEqual(TestFunctions.returns_1(), 1)

    def test_adder_decorator_should_add_10(self):
        self.assertEqual(TestFunctions.returns_1_with_adder(), 11)

    def test_multiplier_decorator_should_multiply_by_2(self):
        self.assertEqual(TestFunctions.returns_1_with_multiplier(), 2)

    def test_adder_then_multiplier_decorators_should_return_22(self):
        self.assertEqual(TestFunctions.returns_1_with_adder_then_multiplier(), 22)

    def test_multiplier_then_adder_decorators_should_return_12(self):
        self.assertEqual(TestFunctions.returns_1_with_multiplier_then_adder(), 12)


class TestFunctions:
    @staticmethod
    def returns_1():
        return 1

    @staticmethod
    @adder
    def returns_1_with_adder():
        return 1

    @staticmethod
    @multiplier
    def returns_1_with_multiplier():
        return 1

    @staticmethod
    @multiplier
    @adder
    def returns_1_with_adder_then_multiplier():
        return 1

    @staticmethod
    @adder
    @multiplier
    def returns_1_with_multiplier_then_adder():
        return 1


if __name__ == '__main__':
    unittest.main()
