from typing import List

from test_framework import generic_test

# 77 mod 64 = 13
# 1001101 mod
# 1000000 =
# 0001101

# Need to set the leftmost values with respect to `mod` to 0

# number mod 4 is the same as number & 00000011
# So get a 1s mask first


def x_mod_power_two(x: int, mod: int) -> int:
    mask = 0
    while mod > 1:
        mask = (mask << 1) ^ 1
        mod >>= 1

    return x & mask


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('4_2_x_mod_power_two.py', '4_2_x_mod_power_two.tsv',
                                       x_mod_power_two))
