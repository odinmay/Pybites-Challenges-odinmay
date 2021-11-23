from collections import Counter


def freq_digit(num: int) -> int:
    counts = Counter(str(num))
    return int(counts.most_common()[0][0])
