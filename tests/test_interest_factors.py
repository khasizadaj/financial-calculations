"""
Test file for interest factors module.

TODO write unit tests for this module.
"""

from decimal import Decimal
from fin_funcs.interest_factors import (pvifa, pvifad)
import fin_funcs.helper_funcs as hf

# annuity factor
return_rate = Decimal("0.02")
number_of_years = 1
int_factor = pvifa(return_rate, number_of_years)
assert hf.quantize(pvifa, 3) == Decimal("0.980")

return_rate = Decimal("0.07")
number_of_years = 7
int_factor = pvifa(return_rate, number_of_years)
assert hf.quantize(pvifa, 3) == Decimal("5.389")

return_rate = Decimal("0.14")
number_of_years = 12
int_factor = pvifa(return_rate, number_of_years)
assert hf.quantize(pvifa, 3) == Decimal("5.660")

# annuity due factor
return_rate = Decimal("0.10")
number_of_years = 3
int_factor = pvifad(return_rate, number_of_years)
assert hf.quantize(pvifad, 3) == Decimal("2.735")
