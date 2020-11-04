from test_framework import generic_test
from typing import List


import sys
import os

sys.path.append(os.getcwd() + '/..')


def can_reach_end(A: List[int]) -> bool:
    # TODO - you fill in here.
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('advance_by_offsets.py',
                                       'advance_by_offsets.tsv',
                                       can_reach_end))
