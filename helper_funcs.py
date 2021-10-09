from decimal import Decimal

def quantize(decimal_number, decimal_count):
    """
    Functions return rounds given decimal number until given decimal count.
    """

    return decimal_number.quantize(Decimal(f'1.{"0"*decimal_count}'))
