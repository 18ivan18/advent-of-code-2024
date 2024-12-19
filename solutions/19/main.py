#!/usr/bin/env python3

from functools import cache
from sys import stdin

towel_patterns = set()


@cache
def is_available(design, max_len):
    if len(design) == 0:
        return 1
    number_of_ways = 0
    for i in range(1, max_len+1):
        if i > len(design):
            break
        prefix = design[:i]
        # print(f"trying {prefix} for {design}")
        if prefix in towel_patterns:
            new_design = design[i:]
            number_of_ways += is_available(new_design, max_len)
    return number_of_ways


def solve():
    a, b = stdin.read().split('\n\n')
    global towel_patterns
    towel_patterns = set([pattern for pattern in a.split(', ')])
    max_len = max([len(pattern) for pattern in towel_patterns])
    deisgns = b.splitlines()
    part_1, part_2 = 0, 0
    for i, design in enumerate(deisgns):
        num_ways = is_available(design, max_len)
        part_1 += 1 if num_ways else 0
        part_2 += num_ways

    print(part_1)
    print(part_2)


if __name__ == '__main__':
    solve()
