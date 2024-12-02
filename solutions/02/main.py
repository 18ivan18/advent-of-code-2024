#!/usr/bin/env python3

from sys import stdin


def is_safe(l: str):
    levels = [int(x) for x in l if x != ' ']
    dec = True
    inc = True

    for i in range(len(levels) - 1):
        if abs(levels[i + 1] - levels[i]) > 3 or abs(levels[i + 1] - levels[i]) < 1:
            return False
        if levels[i + 1] < levels[i]:
            dec = False
        if levels[i + 1] > levels[i]:
            inc = False
    return dec or inc


def get_all_levels(l: str):
    levels = [int(x) for x in l.split()]

    all_levels = []
    for i in range(len(levels)):
        all_levels.append(levels[:i] + levels[i + 1:])
    return all_levels


def solve() -> None:
    input = stdin.read().splitlines()
    print(len([x for x in input if is_safe(x)]))
    print(len([x for x in input if any([is_safe(y) for y in get_all_levels(x)])]))


if __name__ == '__main__':
    solve()
