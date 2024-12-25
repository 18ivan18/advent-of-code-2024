#!/usr/bin/env python3

from sys import stdin


def overlap(a, b):
    for i in range(len(a)):
        if a[i] + b[i] > 5:
            return True
    return False


class Lock():
    def __init__(self, lock):
        self.cols = [0]*5
        for row in lock[1:]:
            for i, c in enumerate(row):
                if c == '#':
                    self.cols[i] += 1


class Key():
    def __init__(self, key):
        self.cols = [0]*5
        for row in key[:-1][::-1]:
            for i, c in enumerate(row):
                if c == '#':
                    self.cols[i] += 1


def solve() -> None:
    input = [[y for y in x.splitlines()] for x in stdin.read().split('\n\n')]
    keys = []
    locks = []
    for obj in input:
        if all(map(lambda x: x == '.', obj[0])):
            keys.append(Key(obj))
        if all(map(lambda x: x == '#', obj[0])):
            locks.append(Lock(obj))
    part_1 = 0
    for lock in locks:
        for key in keys:
            if not overlap(lock.cols, key.cols):
                part_1 += 1
    print(part_1)


if __name__ == '__main__':
    solve()
