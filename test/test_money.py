import unittest


class Money:
    def __init__(self, amount, currency):
        self.amount = amount
        self.currency = currency

    def times(self, multiplier):
        return Money(self.amount * multiplier, self.currency)

    def divide(self, divisor):
        return Money(self.amount / divisor, self.currency)

    def __eq__(self, other):
        return self.amount == other.amount and self.currency == other.currency


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


if __name__ == '__main__':
    unittest.main()
