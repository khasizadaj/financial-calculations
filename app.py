from typing import Dict, Callable
from decimal import Decimal

import fin_funcs.time_value_of_money as tvm
import fin_funcs.helper_funcs as h

TVM_FUNCS = {
    "1": tvm.present_value,
    "2": tvm.present_value_multiple,
    "3": tvm.future_value,
    "4": tvm.number_of_years,
    "5": tvm.return_rate,
    "6": tvm.perpetuity,
    "7": tvm.growing_perpetuity,
    "8": tvm.annuity,
    "9": tvm.annuity_delayed,
}


def calc(func: Callable) -> Decimal:
    """Function gets input parameters from user and returns output."""

    inputs = h.get_parameter_inputs(func)

    res = func(*inputs)
    return res


def get_tvm_func():
    m_start = ["What type of calculation do you want to perform?", "",
               "1. Present Value (PV)", "2. Present Value of Multiple Iregular Cash Flows (PV)",
               "3. Future Value (FV)", "4. Number of years to reach from PV to FV (n)",
               "5. Return rate (r)", "6. Perpetuity", "7. Growing Perpetuity",
               "8. Annuity", "9. Annuity delayed", ""
               ]
    print("\n ".join(m_start))

    func = get_input(TVM_FUNCS)
    return func


FIN_MODULE_FACTORIES = {"1": get_tvm_func, "2": "get_interest_factor_funcs",
                        "3": "get_bond_funcs", "4": "get_share_funcs",
                        "5": "get_npv_funcs"}


def main():
    """Function executes main logic of the application."""

    m_start = ["What type of calculation do you want to perform?", "",
               "1. Time Value of Money", "2. Interest Factors (PVIF, PVIFA)",
               "3. Bond Valuation", "4. Share Valuation",
               "5. NPV and other investment criteria", ""]
    print("\n ".join(m_start))

    mod = get_input(FIN_MODULE_FACTORIES)
    fin_func = mod()

    result = calc(fin_func)
    print(result)


def get_input(dictionary: Dict):
    type_is_correct = False
    while not type_is_correct:
        type_ = input("Write number of calculation type here. (e.g. 2): ")
        mod = dictionary.get(type_, None)
        if mod is not None:
            type_is_correct = True
            break

        print("Please, write correct number.")

    return mod


if __name__ == "__main__":
    main()
