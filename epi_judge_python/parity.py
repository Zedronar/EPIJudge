from test_framework import generic_test


def parity_brute_force(x: int) -> int:
    result = 0
    while x:
        result ^= x & 1
        x >>= 1
    return result

# Erasing the lowest set bit in a word in a single operation
# x & (x-1)

# 2 & 1 =
# 10 & 01 = 00

# 3 & 2 =
# 11 & 10 = 10


def parity(x: int) -> int:
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # Drops the lowest set bit of x.
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
