from typing import List

from test_framework import generic_test


def is_power_of_two(x: int) -> int:
    bit_already_seen = False
    while x:
        if x & 1:
            if bit_already_seen:
                return False
            bit_already_seen = True
        x >>= 1

    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4_3_is_power_of_2.py', '4_3_is_power_of_2.tsv',
                                       is_power_of_two))
