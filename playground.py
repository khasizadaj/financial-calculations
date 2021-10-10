"""
This file is only for trying and calculating questions from the boook.
It's not part of financial calculations package.
"""

from fin_funcs.interest_factors import pvifa
from fin_funcs.helper_funcs import get_decimal, quantize
from fin_funcs.time_value_of_money import get_annuity

# chapter 4, question 16
pv = get_decimal(100_000)
r = get_decimal(0.09)
n = get_decimal(30)
int_fac = quantize(pvifa(r, n), 2)
# print(int_fac)

pm = quantize(pv / int_fac, 2)
# print(pm)

interest_earned = n * pm - pv
# print(interest_earned)


# chapter 4, question 17
cf = get_decimal(1_000)
n = get_decimal(240)
r = get_decimal(0.12/12)
int_fac = quantize(pvifa(r, n), 2)
int_fac = pvifa(r, n)
# print(int_fac)

# random PV calculation
from time_value_of_money import get_present_value
fv = get_decimal(100)
r = get_decimal(0.1)
n = get_decimal(3)
pv = quantize(get_present_value(fv, r, n), 2)
# print(pv)

# random annuity calculation
cf = get_decimal("100")
r = get_decimal("0.1")
n = get_decimal("3.00")
annuity_type = "due"
annuity = get_annuity(cf, r, n, annuity_type)
print(quantize(annuity,2))