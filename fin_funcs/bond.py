"""This module is for bonds related  calculations."""
from decimal import Decimal

import fin_funcs.time_value_of_money as tvm

from .interest_factors import pvifa


def price(face_value: Decimal, coupon_rate: Decimal,
          yield_to_maturity: Decimal, number_of_years: Decimal):
    """Returns present value of bond."""

    coupon = coupon_payment(face_value, coupon_rate)
    interest_factor = pvifa(yield_to_maturity, number_of_years)
    pv_face_value = tvm.present_value(
        face_value, yield_to_maturity, number_of_years)

    result = coupon * interest_factor + pv_face_value

    return result


def coupon_rate(face_value: Decimal, current_price: Decimal,
                yield_to_maturity: Decimal, number_of_years: Decimal):
    """Function returns coupon rate of a given bond."""
    pv_face_value = tvm.present_value(face_value, yield_to_maturity,
                                      number_of_years)

    interest_factor = pvifa(yield_to_maturity, number_of_years)
    interest_payment = (current_price - pv_face_value) / interest_factor

    return interest_payment / face_value


def coupon_payment(face_value: Decimal, coupon_rate: Decimal):
    return face_value * coupon_rate


def rate_of_return(face_value: Decimal, coupon_rate: Decimal, yield_to_maturity: Decimal, original_price: Decimal, number_of_years: Decimal):
    coupon = coupon_payment(face_value, coupon_rate)
    present_value = price(face_value, coupon_rate,
                          yield_to_maturity, number_of_years)
    result = (coupon + present_value - original_price) / original_price
    return result


def real_rate_of_return(nominal_rate: Decimal, inflation_rate: Decimal):
    """Returns real rate of return by considering inflation rate."""

    result = (1 + nominal_rate) / (1 + inflation_rate) - 1
    return result


# from .helper_funcs import quantize
# TEMPLATE: get present value/price of bond

# face_value = Decimal("1000")
# coupon_rate = Decimal("0.09")
# yield_to_maturity = Decimal("0.10")
# number_of_years = Decimal("2.00")

# price_of_bond = price(face_value, coupon_rate,
#                         yield_to_maturity, number_of_years)
# print("Price of bond: ", quantize(price_of_bond, 2))


# TEMPLATE: coupon rate
# face_value = Decimal("1000")
# yield_to_maturity = Decimal("0.08")
# number_of_years = Decimal("8.00")
# selling_price = Decimal("885")

# coupon_rate = coupon_rate(face_value, selling_price, yield_to_maturity, number_of_years)
# print("Coupon rate: ", quantize(coupon_rate, 4))


# TEMPLATE: get return rate

# face_value = Decimal("1000")
# coupon_rate = Decimal("0.09")
# yield_to_maturity = Decimal("0.09")
# number_of_years = Decimal("1")
# orig_price = Decimal("950") # the price that the bond was bought
# number_of_years = Decimal("1.00")

# return_rate = rate_of_return(
#     face_value, coupon_rate, yield_to_maturity, orig_price, number_of_years)

# print("Rate of return", quantize(return_rate, 4))


# TEMPLATE: get real return rate
# it depends on return rate calculations

# inflation = Decimal("0.04")
# return_rate = Decimal("0.07")
# real_return = real_rate_of_return(return_rate, inflation)
# print("Real return: ", quantize(real_return, 4))
