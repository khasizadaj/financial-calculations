"""
Test file for time value of money module.

TODO write unit tests for this module.
"""

from decimal import Decimal
import time_value_of_money as tvm
import helper_funcs as hf

dec_num = Decimal("100000")
assert dec_num.quantize(Decimal("1.00")) == hf.quantize(dec_num, 2)

fv = Decimal("100000")
r = Decimal("0.05")
n = Decimal("20")
pv = tvm.get_present_value(fv, r, n)
assert hf.quantize(pv, 2) == Decimal("37688.95")

pv = Decimal("100")
r = Decimal("0.05")
n = Decimal("10")
fv = tvm.get_future_value(pv, r, n)
assert hf.quantize(fv, 2) == Decimal("162.89")

pv = Decimal("150.00")
fv = Decimal("201.59")
r = Decimal("0.03")
n = tvm.get_numbers_of_years(pv, fv, r)
assert hf.quantize(n, 8) == Decimal("10.00042679")

pv = Decimal("100.00")
fv = Decimal("200.00")
n = Decimal("6.00")
r = tvm.get_return_rate(pv, fv, n)
assert hf.quantize(r, 4) == Decimal("0.1225")

cf = Decimal("1200")
r = Decimal("0.04")
perp = tvm.get_perpetuity(cf, r)
assert hf.quantize(perp, 2) == Decimal("30000.00")

cf = Decimal("1200")
r = Decimal("0.04")
g = Decimal("0.025")
g_perp = tvm.get_growing_perpetuity(cf, r, g)
assert hf.quantize(g_perp, 2) == Decimal("80000.00")
