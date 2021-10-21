"""This module implements interest factors for multiple cash flow models."""

from decimal import Decimal
from typing import Callable


def pvifa(return_rate: Decimal, number_of_periods: Decimal) -> Decimal:
    """Function returns present value interest factor for ordinary annuity."""

    result = Decimal("0.00")

    for i in range(1, int(number_of_periods)+1):
        result += Decimal("1.00") / (Decimal("1.00") +
                                     return_rate) ** Decimal(str(i))

    return result


def pvifad(return_rate: Decimal, number_of_periods: int) -> Decimal:
    """Function returns present value interest factor for annuity due."""

    result = pvifa(return_rate, number_of_periods - 1) + 1

    return result


def get_pvif_func(annuity_type: int) -> Callable:
    """Returns present value interest factor function for given type."""
    if annuity_type == 0:
        return pvifa
    return pvifad

    raise ValueError(
        "Unknown annuity type. Please provide one of these types: ordinary (or deferred), due.")


if __name__ == "__main__":
    from helper_funcs import quantize

    curr_if = pvifa(Decimal("0.02"), 1)
    assert quantize(curr_if, 3) == Decimal("0.980")
