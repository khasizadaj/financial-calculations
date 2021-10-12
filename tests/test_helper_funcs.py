import unittest
from decimal import Decimal

from fin_funcs.helper_funcs import get_decimal, quantize


class TestTimeValueOfMoney(unittest.TestCase):
    """Unittest test for time value of money module."""

    def test_decimal(self):
        expected_value = Decimal("1.00")
        script = get_decimal(1.00)
        self.assertEqual(script, expected_value)

        script = get_decimal("1.00")
        self.assertEqual(script, expected_value)

        script = get_decimal(1)
        self.assertEqual(script, expected_value)

        script = get_decimal(Decimal("1.0"))
        self.assertEqual(script, expected_value)

    def test_quantize(self):
        script = get_decimal("1.1234")
        expected_value = Decimal("1.12345").quantize(Decimal("1.0000"))
        self.assertEqual(quantize(script, 4), expected_value)

        script = get_decimal("1.56")
        expected_value = Decimal("1.5554").quantize(Decimal("1.00"))
        self.assertEqual(quantize(script, 2), expected_value)


if __name__ == '__main__':
    unittest.main()

# dec_num = get_dec("100000")
# assert dec_num.quantize(get_dec("1.00")) == quantize(dec_num, 2)
