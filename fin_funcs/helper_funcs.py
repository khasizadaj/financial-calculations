from decimal import Decimal
from typing import Union, List
import inspect


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

        inp = input(f'Please, provide value of "{arg}": ')
        if annotation is List[Decimal]:
            inputs.append([get_decimal(i) for i in inp.split(",")])
        else:
            inputs.append(get_decimal(inp))
    return inputs
