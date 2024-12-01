#!/usr/bin/env python3

from functools import reduce
from sys import stdin
from typing import Counter


def solve() -> None:
    input = stdin.read().splitlines()
    lists = ([], [])
    for line in input:
        first, second = line.split()
        lists[0].append(int(first))
        lists[1].append(int(second))
    lists = (sorted(lists[0]), sorted(lists[1]))
    total_distance = 0
    for i in range(len(input)):
        total_distance += abs(lists[0][i] - lists[1][i])
    print(total_distance)

    counts = Counter()
    for number in lists[1]:
        counts.update([number])
    print(reduce(lambda x, y: x + y*counts[y], lists[0], 0))


if __name__ == '__main__':
    solve()
