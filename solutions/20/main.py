#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def find(grid, s='S'):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == s:
                return i, j
    raise ValueError('Start not found')


def dfs(grid, x, y):
    stack = [(x, y)]
    path = [(x, y)]
    visited = set()
    while stack:
        x, y = stack.pop()
        visited.add((x, y))
        if grid[x][y] == 'E':
            return path
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not 0 <= nx < len(grid) or not 0 <= ny < len(grid[0]):
                continue
            if grid[nx][ny] == '#':
                continue
            if (nx, ny) in visited:
                continue
            stack.append((nx, ny))
            path.append((nx, ny))
    return path


def solve() -> None:
    grid = [[y for y in x] for x in stdin.read().splitlines()]
    x, y = find(grid, 'S')
    path = dfs(grid, x, y)
    l = len(path)
    distances_part_1, distances_part_2 = defaultdict(int), defaultdict(int)
    part_1_secs, part_2_secs = 2, 20
    for i, (x, y) in enumerate(path):
        for j in range(i+1, len(path)):
            # if manhatan distance is <= 2 we can move there with shortcut
            mhdist = abs(x-path[j][0]) + abs(y-path[j][1])
            if mhdist <= part_1_secs:
                ndist = i + mhdist + (l - j)
                if ndist < l:
                    distances_part_1[l-ndist] += 1
            if mhdist <= part_2_secs:
                ndist = i + mhdist + (l - j)
                if ndist < l:
                    distances_part_2[l-ndist] += 1
    print(sum(distances_part_1[x]
          for x in distances_part_1 if x >= 100))
    print(sum(distances_part_2[x]
          for x in distances_part_2 if x >= 100))


if __name__ == '__main__':
    solve()
