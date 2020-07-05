def sum_numbers(numbers=None):
    if numbers == None:
        return sum(range(101))
    else:
        return sum(numbers)