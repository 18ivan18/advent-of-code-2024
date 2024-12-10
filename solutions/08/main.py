#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def is_inside(x, y, max_x, max_y):
    return x >= 0 and x < max_x and y >= 0 and y < max_y


def solve() -> None:
    input = stdin.read().splitlines()
    nodes = defaultdict(list)
    rows, cols = len(input), len(input[0])
    for i in range(rows):
        for j in range(cols):
            if input[i][j] != '.':
                nodes[input[i][j]].append((i, j))
    antinodes = set()
    for v in nodes.values():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                dx = v[i][0] - v[j][0]
                dy = v[i][1] - v[j][1]
                antinodes.add((v[i][0]+dx, v[i][1]+dy))
                antinodes.add((v[j][0]-dx, v[j][1]-dy))

    print(len([x for x in antinodes if is_inside(x[0], x[1], rows, cols)]))

    antinodes = set()
    for v in nodes.values():
        for i in range(len(v)):
            for j in range(i + 1, len(v)):
                dx = v[i][0] - v[j][0]
                dy = v[i][1] - v[j][1]
                nx, ny = v[i][0], v[i][1]
                while is_inside(nx, ny, rows, cols):
                    antinodes.add((nx, ny))
                    nx += dx
                    ny += dy
                nx, ny = v[j][0], v[j][1]
                while is_inside(nx, ny, rows, cols):
                    antinodes.add((nx, ny))
                    nx -= dx
                    ny -= dy

    print(len(antinodes))


if __name__ == '__main__':
    solve()
