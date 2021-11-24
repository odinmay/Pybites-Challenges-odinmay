from typing import List, TypeVar
T = TypeVar('T', int, float)


def n_digit_numbers(numbers: List[T], n: int) -> List[int]:
    """Take a number and pad digits to n'th value excluding negative sign
    If the value is decimal, strip decimal"""
    number_list = []
    for num in numbers:
        long_n = num * 100000
        print(long_n)
        if str(long_n)[0] == '-':
            number_list.append(int(str(long_n)[:n+1]))
        elif '.' in str(long_n):
            num_str = str(long_n).replace('.', '')
            number_list.append(int(num_str[:n]))
        else:
            number_list.append(int(str(long_n)[:n]))
    return number_list
