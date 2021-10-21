"""
Functions to calculate time value of money.
"""

from decimal import Decimal
from math import log
from typing import List

from .interest_factors import get_pvif_func
from .helper_funcs import get_decimal


def present_val(future_value: Decimal, return_rate: Decimal,
                number_of_periods: int) -> Decimal:
    """Returns the present value of given future value."""

    result = future_value / (1 + return_rate)**number_of_periods
    return result


def present_value_multiple(list_of_future_cash_flows: List[Decimal], return_rate: Decimal):
    """
    Returns present value multiple cash flows in the future.

    Note: If there is no payment in certain period provide 0 for that period as a future
    cash flow.
    """

    result = get_decimal("0.00")
    for number_of_periods, curr_future_value in enumerate(list_of_future_cash_flows, start=1):
        if curr_future_value == 0:
            continue

        curr_pv = present_val(
            curr_future_value, return_rate, number_of_periods)
        result += curr_pv

    return result


def future_val(present_value: Decimal, return_rate: Decimal,
               number_of_periods: int) -> Decimal:
    """Returns the future value of given future value."""

    result = present_value * (1 + return_rate)**number_of_periods
    return result


def number_of_years(present_value: Decimal, future_value: Decimal,
                    return_rate: Decimal) -> Decimal:
    """
    Returns numbers of years needed to get the given future value from given
    present value.
    """
    result: float

    result = log(future_value / present_value, 10) / log(1 + return_rate, 10)
    decimalized_result = Decimal(str(result))
    return decimalized_result


def rate_of_return(present_value: Decimal, future_value: Decimal,
                   number_of_periods: Decimal) -> Decimal:
    """
    Returns the return rate get given future value from given present value
    in given number of years.
    """

    result = (future_value / present_value)**(1 / number_of_periods) - 1
    return result


def perpetuity(annual_cash_flow: Decimal, return_rate: Decimal) -> Decimal:
    """Returns present value of sum of future cash flows."""

    result = annual_cash_flow / return_rate

    return result


def growing_perpetuity(annual_cash_flow: Decimal, return_rate: Decimal,
                       growth_rate: Decimal) -> Decimal:
    """Returns present value of sum of cash flows with growth rate."""

    result = annual_cash_flow / (return_rate - growth_rate)

    return result


def annuity(annual_cash_flow: Decimal, return_rate: Decimal,
            number_of_periods: Decimal, annuity_type: str = 0):
    """Returns present value for given annuity type"""

    pvif_func = get_pvif_func(annuity_type)

    result = annual_cash_flow * pvif_func(return_rate, number_of_periods)

    return result


def annuity_delayed(annual_cash_flow: Decimal, return_rate: Decimal,
                    number_of_periods: Decimal, delay_period: Decimal,
                    annuity_type: str = "ordinary"):
    """Returns present value for given annuity type after certain period pf delay."""

    pvif_func = get_pvif_func(annuity_type)
    if delay_period > 1:
        result = annual_cash_flow * \
            (pvif_func(return_rate, number_of_periods + delay_period - 1) -
             pvif_func(return_rate, delay_period-1))
    else:
        result = annual_cash_flow * pvif_func(return_rate, number_of_periods)

    return result


if __name__ == '__main__':
    print("This module is used to find the time value of money.")
