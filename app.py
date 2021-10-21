from typing import Dict, Callable
from decimal import Decimal

import fin_funcs.time_value_of_money as tvm
import fin_funcs.helper_funcs as h
import fin_funcs.bond as bond
import fin_funcs.interest_factors as int_fac
import fin_funcs.net_present_value as npv
import fin_funcs.share_valuation as share

TVM_FUNCS = {
    "1": tvm.present_val,
    "2": tvm.present_value_multiple,
    "3": tvm.future_val,
    "4": tvm.number_of_years,
    "5": tvm.rate_of_return,
    "6": tvm.perpetuity,
    "7": tvm.growing_perpetuity,
    "8": tvm.annuity,
    "9": tvm.annuity_delayed,
}

SHARE_FUNCS = {
    "1": share.expected_return,
    "2": share.constant_growth_ddm,
    "3": share.rate_of_growth,
    "4": share.ratio_of_payout,
    "5": share.ratio_of_plowback,
    "6": share.pvgo,
}

NPV_FUNCS = {
    "1": npv.npv,
    "2": npv.profitability_index,
    "3": npv.payback_period_same_cash_flow,
}


BOND_FUNCS = {
    "1": bond.price,
    "2": bond.rate_of_coupon,
    "3": bond.coupon_payment,
    "4": bond.rate_of_return,
    "5": bond.real_rate_of_return,
}

INT_FAC_FUNCS = {
    "1": int_fac.pvifa,
    "2": int_fac.pvifad,
}


def get_tvm_func():
    """Returns respective time value of money function based on user input."""

    m_start = ["\n\nWhat type of calculation do you want to perform?", "",
               "1. Present Value (PV)",
               "2. Present Value of Multiple Iregular Cash Flows (PV)",
               "3. Future Value (FV)",
               "4. Number of periods to reach from PV to FV (n)",
               "5. Return rate (r)",
               "6. Perpetuity",
               "7. Growing Perpetuity",
               "8. Annuity", "9. Annuity delayed", ""
               ]
    print("\n ".join(m_start))

    func = h.get_input(TVM_FUNCS)
    return func


def get_interest_factor_funcs():
    """Returns respective interest factor function based on user input."""

    m_start = ["\n\nWhat type of calculation do you want to perform?", "",
               "1. PVIFA",
               "2. PVIFAD", ""
               ]
    print("\n ".join(m_start))

    func = h.get_input(INT_FAC_FUNCS)
    return func


def get_bond_funcs():
    """Returns respective bond valuation function based on user input."""

    m_start = ["\n\nWhat type of calculation do you want to perform?", "",
               "1. Price (PV)",
               "2. Coupon Rate",
               "3. Coupon Payment",
               "4. Rate of return (r)",
               "5. Real rate of return", ""
               ]
    print("\n ".join(m_start))

    func = h.get_input(BOND_FUNCS)
    return func

# NOT READY


def get_share_funcs():
    """Returns respective share valuation function based on user input."""

    m_start = ["\n\nWhat type of calculation do you want to perform?", "",
               "1. Expected return rate (r)",
               "2. Constant Growth Dividend Discount Model (Gordon Model)",
               "3. Growth rate (g)",
               "4. Payout ratio (b)",
               "5. Plowback ratio",
               "6. PVGO", ""
               ]
    print("\n ".join(m_start))

    func = h.get_input(SHARE_FUNCS)
    return func


def get_npv_funcs():
    """
    Returns respective npv and other investment criteria function based on 
    user input.
    """

    m_start = ["\n\nWhat type of calculation do you want to perform?", "",
               "1. Net Present Value(NPV)",
               "2. Profitability index",
               "3. Payback period (same cash flow)", ""
               ]
    print("\n ".join(m_start))

    func = h.get_input(NPV_FUNCS)
    return func


FIN_MODULE_FACTORIES = {"1": get_tvm_func, "2": get_interest_factor_funcs,
                        "3": get_bond_funcs, "4": get_share_funcs,
                        "5": get_npv_funcs}


def main():
    """Function executes main logic of the application."""

    will_continue = True
    while will_continue:
        m_start = ["\nWhat type of calculation do you want to perform?", "",
                   "1. Time Value of Money",
                   "2. Interest Factors (PVIF, PVIFA)",
                   "3. Bond Valuation",
                   "4. Share Valuation",
                   "5. NPV and other investment criteria", ""
                   ]
        print("\n ".join(m_start))

        mod = h.get_input(FIN_MODULE_FACTORIES)
        fin_func = mod()

        result = h.calc(fin_func)
        print(f"Result is {h.quantize(result, 4)}.")

        print("\n======\n")
        will_continue = True if input(
            "Do you want to calculate again? (y/n): ").lower() == "y" else False


if __name__ == "__main__":
    main()
