def number_base_converter(number: str, from_base: int, to_base: int) -> str:
    if not (2 <= from_base <= 36) or not (2 <= to_base <= 36):
        return "ERROR"
    if not number:
        return "ERROR"

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # number -> decimal (do not use int(number, base); read digit by digit)
    decimal_value = 0
    for ch in number.upper():
        pos = digits.find(ch)
        if pos == -1 or pos >= from_base:
            return "ERROR"
        decimal_value = decimal_value * from_base + pos

    if decimal_value == 0:
        return "0"

    # decimal -> to_base
    result = []
    while decimal_value > 0:
        remainder = decimal_value % to_base
        result.append(digits[remainder])
        decimal_value //= to_base

    reversed_result = []
    for i in range(len(result) - 1, -1, -1):
        reversed_result.append(result[i])
    return "".join(reversed_result)
