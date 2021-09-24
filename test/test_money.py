import unittest

from Money import Money


class TestMoney(unittest.TestCase):
    def test_should_multiply(self):
        fiver = Money(5, "USD")
        tenner = Money(10, "USD")
        self.assertEqual(tenner, fiver.times(2))

    def test_should_multiply_in_euros(self):
        tenEuros = Money(10, "EUR")
        twentyEuros = Money(20, "EUR")
        self.assertEqual(twentyEuros, tenEuros.times(2))

    def test_should_divide(self):
        twenty_dollars = Money(20, "USD")
        ten_dollars = Money(10, "USD")
        self.assertEqual(ten_dollars, twenty_dollars.divide(2))

    def test_should_add(self):
        twenty_dollars = Money(20, "USD")
        ten_dollars = Money(10, "USD")
        thirty_dollars = Money(30, "USD")
        self.assertEqual(thirty_dollars, twenty_dollars.add(ten_dollars))


if __name__ == '__main__':
    unittest.main()
