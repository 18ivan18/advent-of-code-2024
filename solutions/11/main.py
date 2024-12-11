#!/usr/bin/env python3

from functools import cache
from sys import stdin

k1 = 25
k2 = 75


def expand_stone(value):
    if value == 0:
        return [1]
    if len(str(value)) % 2 == 0:
        # get the number as string and split it into two parts
        return [int(str(value)[:len(str(value)) // 2]), int(str(value)[len(str(value)) // 2:])]
    return [2024*value]


@cache
def count_stones(value: int, count: int):
    if count == 0:
        return 1
    values = expand_stone(value)
    return sum(count_stones(x, count - 1) for x in values)


def solve():
    input = [int(x) for x in stdin.read().split(' ')]
    print(sum(count_stones(x, k1) for x in input))
    print(sum(count_stones(x, k2) for x in input))


if __name__ == '__main__':
    solve()
