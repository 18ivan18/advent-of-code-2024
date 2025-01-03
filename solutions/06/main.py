#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def is_inside(x, y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y


dirs = [(-1, 0), (0, +1), (+1, 0), (0, -1)]


def get_tile(x, y, grid, direction):
    try:
        dx, dy = dirs[direction]
        return grid[x+dx][y+dy]
    except:
        return '.'


def solve() -> None:
    input = [[y for y in line] for line in stdin.read().splitlines()]
    for i in range(len(input)):
        for j in range(len(input[i])):
            if input[i][j] == '^':
                start_x, start_y = i, j
                break
    max_x, max_y, direction = len(input), len(input[0]), 0
    visited = set()

    x, y = start_x, start_y
    while is_inside(x, y, max_x, max_y):
        visited.add((x, y))
        tile = get_tile(x, y, input, direction)
        if tile == '#':
            direction = (direction + 1) % 4

        dx, dy = dirs[direction]
        x += dx
        y += dy
    print(len(visited))

    possible = 0
    for v in visited:
        obstacle_x, obstacle_y = v
        input[obstacle_x][obstacle_y] = '#'
        x, y, direction = start_x, start_y, 0
        visited = set()
        while is_inside(x, y, max_x, max_y):
            if (x, y, direction) in visited:
                possible += 1
                break
            visited.add((x, y, direction))

            tile = get_tile(x, y, input, direction)
            if tile == '#':
                direction = (direction + 1) % 4
                continue

            dx, dy = dirs[direction]
            x += dx
            y += dy

        input[obstacle_x][obstacle_y] = '.'
    print(possible)


if __name__ == '__main__':
    solve()
