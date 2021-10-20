from decimal import Decimal, InvalidOperation
from typing import Union, List, Callable, Dict

import inspect
import sys


def quantize(decimal_number, decimal_count):
    """
    Functions return rounds given decimal number until given decimal count.
    """

    return decimal_number.quantize(Decimal(f'1.{"0"*decimal_count}'))


def get_decimal(value: Union[Decimal, int, float, str]) -> Decimal:
    """Return decimal representation of given value."""

    if isinstance(value, Decimal):
        return value
    elif isinstance(value, int) or isinstance(value, float):
        return Decimal(str(value))
    elif isinstance(value, str):
        return Decimal(value)

    raise ValueError("Please provide correct value type. For example: 1.00")


def get_parameter_inputs(func) -> List:
    """Returns list of parameter inputs for the given function from user"""

    specs = inspect.getfullargspec(func)

    inputs = []
    for arg, annotation in zip(specs.args, specs.annotations.values()):

        try:
            if annotation is List[Decimal]:
                inp = input(
                    f'Please, provide value of "{arg}" (seperate them with commas): ')
                inputs.append([get_decimal(i)
                               for i in inp.replace(" ", "").split(",")])
            else:
                inp = input(f'Please, provide value of "{arg}": ')
                inputs.append(get_decimal(inp))
        except InvalidOperation:
            print("Invalid input (not decimal number) passed. Please, provide correct value (e.g. 1.00 or 100). If list of values asked, use comma as seperator.")
            sys.exit()
    return inputs


def calc(func: Callable) -> Decimal:
    """Function gets input parameters from user and returns output."""

    inputs = get_parameter_inputs(func)

    res = func(*inputs)
    return res


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
