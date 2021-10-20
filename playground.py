"""
This file is only for trying and calculating questions from the boook.
It's not part of financial calculations package.
"""

from fin_funcs.interest_factors import pvifa
from fin_funcs.helper_funcs import get_decimal, quantize
from fin_funcs.time_value_of_money import annuity, present_value, present_value_multiple

# return_rate = get_decimal("0.08")
# pv_sum = present_value_multiple([get_decimal(500), get_decimal(600), get_decimal(700)], return_rate)
# print("pv_sum: %s" % pv_sum)

rate = get_decimal("0.1268") / get_decimal("12")
n = get_decimal("60")
int_fac = pvifa(rate, n)
print(int_fac)
print(get_decimal("10000")/int_fac)

# # chapter 4, question 16
# pv = get_decimal(100_000)
# r = get_decimal(0.09)
# n = get_decimal(30)
# int_fac = quantize(pvifa(r, n), 2)
# # print(int_fac)

# pm = quantize(pv / int_fac, 2)
# # print(pm)

# interest_earned = n * pm - pv
# # print(interest_earned)


# # chapter 4, question 17
# cf = get_decimal(1_000)
# n = get_decimal(240)
# r = get_decimal(0.12/12)
# int_fac = quantize(pvifa(r, n), 2)
# int_fac = pvifa(r, n)
# # print(int_fac)

# # random PV calculation
# fv = get_decimal(100)
# r = get_decimal(0.1)
# n = get_decimal(3)
# pv = quantize(present_value(fv, r, n), 2)
# # print(pv)

# # random annuity calculation
# cf = get_decimal("1200")
# r = get_decimal("0.06")
# n = get_decimal("7.00")
# annuity = annuity(cf, r, n)
# print("10 years, 1000, 6%: ", quantize(annuity,2))

# # annuity

