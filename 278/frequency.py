from collections import Counter


def major_n_minor(numbers):
    """
    Input: an array with integer numbers
    Output: the majority and minority number
    """
    counts = Counter(numbers).most_common()
    most_common = counts[0][0]
    least_common = counts[-1][0]

    return most_common, least_common
