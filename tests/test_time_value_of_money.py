"""
Test file for time value of money module.
"""

import unittest

from fin_funcs import time_value_of_money as tvm
from fin_funcs.helper_funcs import get_decimal as get_dec, quantize


class TestTimeValueOfMoney(unittest.TestCase):
    """Unittest test for time value of money module."""

    def test_get_present_value(self):
        future_value = get_dec("100000")
        rate = get_dec("0.05")
        num_of_years = get_dec("20")

        script = tvm.present_value(future_value, rate, num_of_years)
        real = get_dec("37688.95")
        self.assertEqual(quantize(script, 2), real)

    def test_get_future_value(self):
        present_value = get_dec("100")
        return_rate = get_dec("0.05")
        number_of_years = get_dec("10")

        script = tvm.future_value(
            present_value, return_rate, number_of_years)
        real = get_dec("162.89")
        self.assertEqual(quantize(script, 2), real)

    def test_get_number_of_years(self):
        present_value = get_dec("150.00")
        future_value = get_dec("201.59")
        return_rate = get_dec("0.03")

        script = tvm.number_of_years(
            present_value, future_value, return_rate)
        real = get_dec("10.00042679")
        self.assertEqual(quantize(script, 8), real)

    def test_get_return_rate(self):
        present_value = get_dec("100.00")
        future_value = get_dec("200.00")
        number_of_years = get_dec("6.00")

        script = tvm.return_rate(
            present_value, future_value, number_of_years)
        real = get_dec("0.1225")
        self.assertEqual(quantize(script, 4), real)

    def test_get_perpetuity(self):
        cash_flow = get_dec("1200")
        return_rate = get_dec("0.04")

        script = tvm.perpetuity(cash_flow, return_rate)
        expected_value = get_dec("30000.00")
        self.assertEqual(quantize(script, 2), expected_value)

    def test_get_growing_perpetuity(self):
        cash_flow = get_dec("1200")
        return_rate = get_dec("0.04")
        growth_rate = get_dec("0.025")
        script = tvm.growing_perpetuity(
            cash_flow, return_rate, growth_rate)
        expected_value = get_dec("80000.00")
        self.assertEqual(quantize(script, 2), expected_value)

    def test_get_annuity(self):
        # ordinary annuity
        cash_flow = get_dec("100")
        return_rate = get_dec("0.1")
        number_of_years = get_dec("3.00")
        annuity_type = "ordinary"

        script = tvm.annuity(
            cash_flow, return_rate, number_of_years, annuity_type)
        expected_value = get_dec("248.6852")
        self.assertEqual(quantize(script, 4), expected_value)

        # annuity due
        cash_flow = get_dec("100")
        return_rate = get_dec("0.1")
        number_of_years = get_dec("3.00")
        annuity_type = "due"

        script = tvm.annuity(
            cash_flow, return_rate, number_of_years, annuity_type)
        expected_value = get_dec("273.5537")
        self.assertEqual(quantize(script, 4), expected_value)

        # wrong annuity type
        cash_flow = get_dec("100")
        return_rate = get_dec("0.1")
        number_of_years = get_dec("3.00")
        annuity_type = "wrong type"

        self.assertRaises(ValueError, tvm.annuity, cash_flow,
                          return_rate, number_of_years, annuity_type)

    def test_get_annuity_delayed(self):
        cash_flow = get_dec("100")
        return_rate = get_dec("0.07")
        number_of_years = get_dec("5.00")
        delay_period = get_dec("2.00")

        script = tvm.annuity_delayed(
            cash_flow, return_rate, number_of_years, delay_period)
        expected_value = get_dec("383.20")
        self.assertEqual(quantize(script, 2), expected_value)

        # 1 year delay / normal situation
        delay_period = get_dec("1.00")
        script = tvm.annuity_delayed(
            cash_flow, return_rate, number_of_years, delay_period)
        expected_value = get_dec("410.02")
        self.assertEqual(quantize(script, 2), expected_value)

    def test_get_present_value_multiple(self):
        cash_flows = [get_dec(cash_flow) for cash_flow in [100, 100, 100]]
        return_rate = get_dec("0.1")

        script = tvm.present_value_multiple(cash_flows, return_rate)
        expected_value = tvm.annuity(
            get_dec("100"), return_rate, get_dec("3"))
        self.assertEqual(quantize(script, 2), quantize(expected_value, 2))

        # no payment in certain period
        no_payment = get_dec("0.0")
        cf_1 = get_dec("100")
        cf_2 = get_dec("100")
        cf_3 = get_dec("100")
        return_rate = get_dec("0.1")

        script = tvm.present_value_multiple(
            [cf_1, cf_2, no_payment, cf_3], return_rate)
        expected_value = tvm.present_value(cf_1, return_rate, 1) + tvm.present_value(
            cf_2, return_rate, 2) + tvm.present_value(cf_3, return_rate, 4)
        self.assertEqual(quantize(script, 2), quantize(expected_value, 2))


if __name__ == "__main__":
    unittest.main()
