#!/usr/bin/env python3

from collections import defaultdict
from heapq import heapify, heappop, heappush
from sys import stdin


def find(grid, s='S'):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == s:
                return i, j
    raise ValueError('Start not found')


LEFT = (0, -1)
RIGHT = (0, 1)
UP = (-1, 0)
DOWN = (1, 0)
directions = [RIGHT, UP, DOWN, LEFT]


def dijkstra(grid, x, y, ex, ey):
    dist = defaultdict(lambda: float('inf'))
    dist[(x, y)] = 0
    # start facing EAST...
    pq = [(0, x, y, RIGHT, [(x, y)])]
    paths = []
    best_score = float('inf')

    while pq:
        current_distance, x, y, direction, path = heappop(pq)
        if x == ex and y == ey:
            best_score = current_distance
            paths.append(path)
            continue
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if grid[nx][ny] == '#':
                continue
            if (nx, ny) in path:
                continue
            new_distance = current_distance + 1
            if direction != (dx, dy):
                new_distance += 1000
            if new_distance < dist[(nx, ny)]:
                dist[(nx, ny)] = new_distance
                heappush(pq, (new_distance, nx, ny, (dx, dy), path+[(nx, ny)]))
    return best_score, paths


def solve():
    global grid
    grid = [[y for y in x] for x in stdin.read().splitlines()]
    sx, sy = find(grid, 'S')
    ex, ey = find(grid, 'E')
    best_scroe, paths = dijkstra(grid, sx, sy, ex, ey)
    print(best_scroe)
    best_seats = set()
    for path in paths:
        best_seats |= set(path)
    print(len(best_seats))


if __name__ == '__main__':
    solve()
