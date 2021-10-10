"""
Test file for time value of money module.

TODO write unit tests for this module.
"""

from decimal import Decimal
import time_value_of_money as tvm
import helper_funcs as hf

dec_num = Decimal("100000")
assert dec_num.quantize(Decimal("1.00")) == hf.quantize(dec_num, 2)

future_value = Decimal("100000")
return_rate = Decimal("0.05")
number_of_years = Decimal("20")
present_value = tvm.get_present_value(
    future_value, return_rate, number_of_years)
assert hf.quantize(present_value, 2) == Decimal("37688.95")

present_value = Decimal("100")
return_rate = Decimal("0.05")
number_of_years = Decimal("10")
future_value = tvm.get_future_value(
    present_value, return_rate, number_of_years)
assert hf.quantize(future_value, 2) == Decimal("162.89")

present_value = Decimal("150.00")
future_value = Decimal("201.59")
return_rate = Decimal("0.03")
number_of_years = tvm.get_numbers_of_years(
    present_value, future_value, return_rate)
assert hf.quantize(number_of_years, 8) == Decimal("10.00042679")

present_value = Decimal("100.00")
future_value = Decimal("200.00")
number_of_years = Decimal("6.00")
return_rate = tvm.get_return_rate(present_value, future_value, number_of_years)
assert hf.quantize(return_rate, 4) == Decimal("0.1225")

cash_flow = Decimal("1200")
return_rate = Decimal("0.04")
perp = tvm.get_perpetuity(cash_flow, return_rate)
assert hf.quantize(perp, 2) == Decimal("30000.00")

cash_flow = Decimal("1200")
return_rate = Decimal("0.04")
growth_rate = Decimal("0.025")
growing_perp = tvm.get_growing_perpetuity(cash_flow, return_rate, growth_rate)
assert hf.quantize(growing_perp, 2) == Decimal("80000.00")

# ordinary annuity
cash_flow = Decimal("100")
return_rate = Decimal("0.1")
number_of_years = 3
annuity_type = "ordinary"
annuity = tvm.get_annuity(cash_flow, return_rate,
                          number_of_years, annuity_type)
assert hf.quantize(annuity, 4) == Decimal("248.6852")

cash_flow = Decimal("100")
return_rate = Decimal("0.1")
number_of_years = 3
annuity_type = "due"
annuity = tvm.get_annuity(cash_flow, return_rate,
                          number_of_years, annuity_type)
assert hf.quantize(annuity, 4) == Decimal("273.5537")

# checking annuity type error
cash_flow = Decimal("100")
return_rate = Decimal("0.1")
number_of_years = 3
annuity_type = "wrong"
try:
    annuity = tvm.get_annuity(cash_flow, return_rate,
                              number_of_years, annuity_type)
except ValueError as e:
    print(e)
