import itertools
from pprint import pprint

def find_number_pairs(numbers, N=10):
    pairs = []
    gen_boi = itertools.combinations(numbers, 2)
    for pair in gen_boi:
        if sum(pair) == N:
            pairs.append(pair)
    return pairs


