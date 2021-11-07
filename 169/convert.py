def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    if not isinstance(value, int):
        if not isinstance(value, float):
            raise TypeError

    if fmt.lower() == "in":
        value /= 2.54
        return float(round(value, 4))

    elif fmt.lower() == "cm":
        result = value * 2.54
        return float(round(result, 4))

    else:
        raise ValueError
