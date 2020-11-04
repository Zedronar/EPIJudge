from typing import List

from test_framework import generic_test


def right_propagate(x: int) -> int:
    propagated_x = x
    counter = 0
    while not (x & 1):
        propagated_x |= (1 << counter)
        counter += 1
        x >>= 1

    return propagated_x


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4_1_right_propagate.py', '4_1_right_propagate.tsv',
                                       right_propagate))
