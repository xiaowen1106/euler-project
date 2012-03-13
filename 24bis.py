def prob24():
    """
    What is the millionth lexicographic permutation
    of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
    """
    from itertools import permutations
    count = 0
    for perm in permutations('0123456789'):
        count += 1
        if count == 1000000:
            return ''.join(list(perm))

prob(24)
