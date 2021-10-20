"""This module is used to calculate net present value other investment criterion."""

from decimal import Decimal
from typing import List

from . import time_value_of_money as tvm
from . import helper_funcs as h


def npv(initial_investment: Decimal, rate_of_return: Decimal, list_of_future_cash_flows: List[Decimal]):
    total_pv = tvm.present_value_multiple(
        list_of_future_cash_flows, rate_of_return)
    return total_pv - initial_investment


def profitability_index(present_value_of_cash_flows: Decimal, initial_investment: Decimal):
    return present_value_of_cash_flows / initial_investment


def payback_period_same_cash_flow(initial_investment: Decimal, cash_flow: Decimal):
    return initial_investment / cash_flow


# import .interest_factors as i_f
# print(i_f.pvifa(Decimal("0.15"), Decimal("5")))

# Template: NPV
# inv = h.get_decimal(800)
# r = h.get_decimal(0.194)
# cash_flows = [h.get_decimal(i) for i in [100, 100, 1_100]]
# npv_c = npv(inv, r, cash_flows)
# print(h.quantize(npv_c, 2))


# Template:Profitability Index
# cash_flows = [Decimal("3500"), Decimal(
#     "3500"), Decimal("3500"), Decimal("3500")]
# r = Decimal("0.1")
# pv_cash_flows = tvm.present_value_multiple(cash_flows, r)
# inv = Decimal("10000")

# index = profitability_index(pv_cash_flows, inv)
# print(h.quantize(index, 2))


# Template: Payback Period - Same Cash Flow
# inv = Decimal("10000")
# cash_flow = Decimal("3500")
# payback_period = payback_period_same_cash_flow(inv, cash_flow)
# print(h.quantize(payback_period, 2))
