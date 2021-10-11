"""
Functions to calculate time value of money.

TODO Write function to calculate multiple cash flows.
"""

from decimal import Decimal
from math import log
from typing import List

from .interest_factors import get_pvif_func
from .helper_funcs import get_decimal


def get_present_value(future_value: Decimal, return_rate: Decimal,
                      number_of_years: int) -> Decimal:
    """Returns the present value of given future value."""

    result = future_value / (1 + return_rate)**number_of_years
    return result


def get_present_value_multiple(future_cash_flows: List[Decimal], return_rate: Decimal):
    """
    Returns present value multiple cash flows in the future.
    
    Note: If there is no payment in certain period provide 0 for that period as a future
    cash flow.
    """

    result = get_decimal("0.00")
    for number_of_years, curr_future_value in enumerate(future_cash_flows, start=1):
        if curr_future_value == 0:
            continue

        curr_pv = get_present_value(
            curr_future_value, return_rate, number_of_years)
        result += curr_pv

    return result


def get_future_value(present_value: Decimal, return_rate: Decimal,
                     number_of_years: int) -> Decimal:
    """Returns the future value of given future value."""

    result = present_value * (1 + return_rate)**number_of_years
    return result


def get_number_of_years(present_value: Decimal, future_value: Decimal,
                        return_rate: Decimal) -> Decimal:
    """
    Returns numbers of years needed to get the given future value from given
    present value.
    """
    result: float

    result = log(future_value / present_value, 10) / log(1 + return_rate, 10)
    decimalized_result = Decimal(str(result))
    return decimalized_result


def get_return_rate(present_value: Decimal, future_value: Decimal,
                    number_of_years: Decimal) -> Decimal:
    """
    Returns the return rate get given future value from given present value
    in given number of years.
    """

    result = (future_value / present_value)**(1 / number_of_years) - 1
    return result


def get_perpetuity(cash_flow: Decimal, return_rate: Decimal) -> Decimal:
    """Returns present value of sum of future cash flows."""

    result = cash_flow / return_rate

    return result


def get_growing_perpetuity(cash_flow: Decimal, return_rate: Decimal,
                           growth_rate: Decimal) -> Decimal:
    """Returns present value of sum of cash flows with growth rate."""

    result = cash_flow / (return_rate - growth_rate)

    return result


def get_annuity(cash_flow: Decimal, return_rate: Decimal,
                number_of_years: Decimal, annuity_type: str = "ordinary"):
    """Returns present value for given annuity type"""

    pvif_func = get_pvif_func(annuity_type)

    result = cash_flow * pvif_func(return_rate, number_of_years)

    return result


def get_annuity_delayed(cash_flow: Decimal, return_rate: Decimal,
                        number_of_years: Decimal, delay_period: Decimal,
                        annuity_type: str = "ordinary"):
    """Returns present value for given annuity type after certain period pf delay."""

    pvif_func = get_pvif_func(annuity_type)
    if delay_period > 1:
        result = cash_flow * \
            (pvif_func(return_rate, number_of_years + delay_period - 1) -
             pvif_func(return_rate, delay_period-1))
    else:
        result = cash_flow * pvif_func(return_rate, number_of_years)

    return result


if __name__ == '__main__':
    print("This module is used to find the time value of money.")
