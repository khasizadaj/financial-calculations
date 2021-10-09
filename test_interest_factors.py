"""
Test file for interest factors module.

TODO write unit tests for this module.
"""

from decimal import Decimal
import interest_factors
import helper_funcs as hf

return_rate = Decimal("0.02")
number_of_years = 1
pvifa = interest_factors.pvifa(return_rate, number_of_years)
assert hf.quantize(pvifa, 3) == Decimal("0.980")

return_rate = Decimal("0.07")
number_of_years = 7
pvifa = interest_factors.pvifa(return_rate, number_of_years)
assert hf.quantize(pvifa, 3) == Decimal("5.389")

return_rate = Decimal("0.14")
number_of_years = 12
pvifa = interest_factors.pvifa(return_rate, number_of_years)
assert hf.quantize(pvifa, 3) == Decimal("5.660")

return_rate = Decimal("0.10")
number_of_years = 3
pvifad = interest_factors.pvifad(return_rate, number_of_years)
assert hf.quantize(pvifad, 3) == Decimal("2.735")
