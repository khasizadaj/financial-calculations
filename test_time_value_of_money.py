"""
Test file for time value of money module.

TODO write unit tests for this module.
"""

from decimal import Decimal
import time_value_of_money as tvm
from helper_funcs import get_decimal, quantize


dec_num = get_decimal("100000")
assert dec_num.quantize(get_decimal("1.00")) == quantize(dec_num, 2)

# # Single cash flow
# finding future value
future_value = get_decimal("100000")
return_rate = get_decimal("0.05")
number_of_years = get_decimal("20")
present_value = tvm.get_present_value(
    future_value, return_rate, number_of_years)
assert quantize(present_value, 2) == get_decimal("37688.95")

# finding present value
present_value = get_decimal("100")
return_rate = get_decimal("0.05")
number_of_years = get_decimal("10")
future_value = tvm.get_future_value(
    present_value, return_rate, number_of_years)
assert quantize(future_value, 2) == get_decimal("162.89")

# finding required years
present_value = get_decimal("150.00")
future_value = get_decimal("201.59")
return_rate = get_decimal("0.03")
number_of_years = tvm.get_numbers_of_years(
    present_value, future_value, return_rate)
assert quantize(number_of_years, 8) == get_decimal("10.00042679")

# finding return rate
present_value = get_decimal("100.00")
future_value = get_decimal("200.00")
number_of_years = get_decimal("6.00")
return_rate = tvm.get_return_rate(present_value, future_value, number_of_years)
assert quantize(return_rate, 4) == get_decimal("0.1225")

# # Multiple cash flows
# simple perpetuity
cash_flow = get_decimal("1200")
return_rate = get_decimal("0.04")
perp = tvm.get_perpetuity(cash_flow, return_rate)
assert quantize(perp, 2) == get_decimal("30000.00")

# growing perpetuity
cash_flow = get_decimal("1200")
return_rate = get_decimal("0.04")
growth_rate = get_decimal("0.025")
growing_perp = tvm.get_growing_perpetuity(cash_flow, return_rate, growth_rate)
assert quantize(growing_perp, 2) == get_decimal("80000.00")

# ordinary annuity
cash_flow = get_decimal("100")
return_rate = get_decimal("0.1")
number_of_years = get_decimal("3.00")
annuity_type = "ordinary"
annuity = tvm.get_annuity(cash_flow, return_rate,
                          number_of_years, annuity_type)
assert quantize(annuity, 4) == get_decimal("248.6852")

# annutiy due
cash_flow = get_decimal("100")
return_rate = get_decimal("0.1")
number_of_years = get_decimal("3.00")
annuity_type = "due"
annuity = tvm.get_annuity(cash_flow, return_rate,
                          number_of_years, annuity_type)
assert quantize(annuity, 4) == get_decimal("273.5537")

# checking annuity type error
cash_flow = get_decimal("100")
return_rate = get_decimal("0.1")
number_of_years = get_decimal("3.00")
annuity_type = "wrong"
try:
    annuity = tvm.get_annuity(cash_flow, return_rate,
                              number_of_years, annuity_type)
except ValueError as e:
    print(e)
