"""This module implements interest factors for multiple cash flow models."""

from decimal import Decimal


def pvifa(return_rate: Decimal, number_of_years: int) -> Decimal:
    """Function returns present value interest factor for ordinary annuity."""

    result = Decimal("0.00")

    for i in range(1, number_of_years+1):
        result += Decimal("1.00") / (Decimal("1.00") +
                                     return_rate) ** Decimal(str(i))

    return result


def pvifad(return_rate: Decimal, number_of_years: int) -> Decimal:
    """Function returns present value interest factor for annuity due."""

    result = pvifa(return_rate, number_of_years - 1) + 1
    
    return result


if __name__ == "__main__":
    from helper_funcs import quantize

    curr_if = pvifa(Decimal("0.02"), 1)
    assert quantize(curr_if, 3) == Decimal("0.980")
