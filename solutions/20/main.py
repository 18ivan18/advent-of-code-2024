#!/usr/bin/env python3

from copy import deepcopy
from sys import stdin


def find(grid, s='S'):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == s:
                return i, j
    raise ValueError('Start not found')


def dfs(grid, x, y, visited=set(), cheats=1):
    stack = [(x, y, 1)]
    c = []
    while stack:
        x, y, dist = stack.pop()
        visited.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < len(grid) or not 0 <= ny < len(grid[0]):
                continue
            if grid[nx][ny] == 'E':
                return dist, c
            if grid[nx][ny] == '#':
                if cheats > 0:
                    ps, _ = dfs(grid, nx, ny, deepcopy(visited), cheats - 1)
                    if ps > 0:
                        c.append(ps+dist)
                continue
            if (nx, ny) in visited:
                continue
            stack.append((nx, ny, dist+1))
    return 0, c


def solve() -> None:
    grid = [[y for y in x] for x in stdin.read().splitlines()]
    x, y = find(grid, 'S')

    control, cheat_values = dfs(grid, x, y)
    cheat_values = [control - x for x in cheat_values]
    cheat_values = {x: cheat_values.count(x) for x in set(cheat_values)}

    # print(control, cheat_values)
    # print number of cheats that are >=100
    print(sum(cheat_values[x] for x in cheat_values if x >= 100))


if __name__ == '__main__':
    solve()
