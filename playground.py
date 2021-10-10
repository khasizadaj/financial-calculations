"""
This file is only for trying and calculating questions from the boook.
It's not part of financial calculations package.
"""

from interest_factors import pvifa
from helper_funcs import get_decimal, quantize

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
print(int_fac)

