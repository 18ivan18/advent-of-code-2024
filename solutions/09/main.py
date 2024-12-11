#!/usr/bin/env python3

from copy import deepcopy
from sys import stdin


def get_checksum(memory):
    checksum = 0
    idx = 0
    for i in range(len(memory)):
        for _ in range(memory[i][0]):
            if memory[i][2] == 'taken':
                checksum += idx * memory[i][1]
            idx += 1
    return checksum


def part_1(memory: list):
    j, nmem = len(memory) - 1, []
    for i in range(len(memory)):
        if i > j:
            break
        m = memory[i]
        if m[2] == 'free':
            # look for taken spaces at the end
            while j >= 0:
                times, idx, state = memory[j]
                if times == 0:
                    j -= 1
                    continue
                if state == 'taken':
                    if m[0] > times:
                        nmem.append((times, idx, 'taken'))
                        m[0] -= times
                        memory[j][2] = 'free'
                    elif m[0] <= times:
                        nmem.append((m[0], idx, 'taken'))
                        memory[j][0] -= m[0]
                        m[0] = 0
                        break
                j -= 1
        if m[2] == 'taken' and m[0] > 0:
            nmem.append(m)
    return get_checksum(nmem)


def part_2(memory: list):
    new_memory, visited = [], set()
    for i, m in enumerate(memory):
        _, _, curr_state = m
        if curr_state == 'free':
            if i in visited:
                new_memory.append(m)
                continue
            # look for blocks at the end
            j = len(memory) - 1
            while j >= 0 and i < j:
                times, idx, state = memory[j]
                if state == 'taken' and m[0] >= times:
                    new_memory.append((times, idx, 'taken'))
                    m[0] -= times
                    memory[j][2] = 'free'
                    visited.add(j)
                if m[0] == 0:
                    break
                j -= 1
            if m[0] != 0:
                new_memory.append(m)
        if curr_state == 'taken' and m[0] > 0:
            new_memory.append(m)
    return get_checksum(new_memory)


def solve() -> None:
    input = stdin.read()
    memory = []
    id = 0
    for i in range(len(input)):
        if i % 2 == 0:
            memory.append([int(input[i]), id, 'taken'])
            id += 1
        else:
            memory.append([int(input[i]), -1, 'free'])
    print(part_1(deepcopy(memory)))
    print(part_2(deepcopy(memory)))


if __name__ == '__main__':
    solve()
