#!/usr/bin/env python3

from sys import stdin


def is_inside(x, y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y


def trail(grid, start_x, start_y):
    # write a basic DFS, we can only go up, down, left, right
    # the numbers must be higher than the current one
    # use backtracking to find all different paths
    max_x, max_y = len(grid), len(grid[0])
    stack = [(start_x, start_y)]
    visited = set()
    res = 0
    while stack:
        x, y = stack.pop()
        if grid[x][y] == '9':
            res += 1
        visited.add((x, y))
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if not is_inside(nx, ny, max_x, max_y):
                continue
            if (nx, ny) in visited:
                continue
            if int(grid[nx][ny]) != int(grid[x][y]) + 1:
                continue
            stack.append((nx, ny))
    return res


def trail_rec(grid, x, y, prev: int = -1):
    # move in a maze, we can only go up, down, left, right
    # the next number must be one higher than the current one
    # use backtracking to find all different paths fro start to 9
    max_x, max_y = len(grid), len(grid[0])
    res = 0
    if not is_inside(x, y, max_x, max_y):
        return 0
    if prev + 1 != int(grid[x][y]):
        return 0
    if grid[x][y] == '9':
        return 1
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        nx, ny = x + dx, y + dy
        res += trail_rec(grid, nx, ny, int(grid[x][y]))
    return res


def solve() -> None:
    input = stdin.read().splitlines()
    part_1, part_2 = 0, 0
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '0':
                part_1 += trail(input, i, j)
                part_2 += trail_rec(input, i, j)
    print(part_1)
    print(part_2)


if __name__ == '__main__':
    solve()
