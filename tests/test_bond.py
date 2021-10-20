import unittest

from fin_funcs.helper_funcs import get_decimal as get_dec, quantize
from fin_funcs.bond import price


class TestTimeValueOfMoney(unittest.TestCase):
    """Unittest test for time value of money module."""

    def test_present_value(self):
        face = get_dec("1000")
        c = get_dec("0.09")
        r = get_dec("0.12")
        n = get_dec("6.00")
        script = price(face, c, r, n)
        expected_value = get_dec("876.66")
        self.assertEqual(quantize(script, 2), expected_value)


if __name__ == '__main__':
    unittest.main()
