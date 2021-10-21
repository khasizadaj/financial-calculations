from decimal import Decimal


def expected_return(dividend_amount: Decimal, new_price: Decimal, original_price: Decimal):
    """Returns expected return for share."""

    return (dividend_amount + new_price - original_price) / original_price


def constant_growth_ddm(dividend_amount: Decimal, rate_of_return: Decimal,
                        growth_rate: Decimal, dividend_is_gonna_grow: Decimal):
    """Calculates price of dividend with given constant growth rate."""

    if dividend_is_gonna_grow == Decimal("1"):
        dividend_amount *= (1 + growth_rate)

    denominator = rate_of_return - growth_rate
    return dividend_amount / denominator


script = constant_growth_ddm(Decimal("2.00"), Decimal(
    "0.1"), Decimal("0.06"), Decimal("1"))
assert script == Decimal("53")


def rate_of_growth(return_on_equity: Decimal, plowback_ratio: Decimal) -> Decimal:
    return return_on_equity * plowback_ratio


script = rate_of_growth(Decimal("0.12"), Decimal("0.45"))
assert script == Decimal("0.054")


def ratio_of_payout(dividend_amount: Decimal, earning_per_share: Decimal) -> Decimal:
    return dividend_amount / earning_per_share


script = ratio_of_payout(Decimal("3"), Decimal("5.0"))
assert script == Decimal("0.6")


def ratio_of_plowback(dividend_amount: Decimal, earning_per_share: Decimal) -> Decimal:
    return 1 - ratio_of_payout(dividend_amount, earning_per_share)


script = ratio_of_plowback(Decimal("3.0"), Decimal("5.0"))
assert script == Decimal("0.4")


def pvgo(dividend_amount: Decimal, earning_per_share: Decimal, rate_of_return: Decimal, growth_rate, dividend_is_gonna_grow: Decimal) -> Decimal:
    if dividend_is_gonna_grow == Decimal("1"):
        dividend_amount *= (1 + growth_rate)

    with_growth = constant_growth_ddm(dividend_amount, rate_of_return,
                                      growth_rate, dividend_is_gonna_grow)

    no_growth = earning_per_share / rate_of_return
    return with_growth - no_growth


script = pvgo(Decimal("336.0"), Decimal("840.0"),
              Decimal(".16"), Decimal("0.12"), Decimal("0"))
assert script == Decimal("3150")
