#!/usr/bin/env python3

from sys import stdin

dirs = [(1, 0), (-1, 0), (0, 1),  (0, -1)]
dirs_map = {(1, 0): 'up', (-1, 0): 'down', (0, 1): 'left', (0, -1): 'right'}


def number_of_sides(sides: list[tuple]):
    visited = set()
    s = 0
    for x, y, dir in sides:
        if (x, y, dir) in visited:
            continue
        s += 1
        original_x, original_y = x, y
        if (dir == 'down' or dir == 'up'):
            x, y = original_x, original_y
            while (x, y, dir) in sides:
                # going right
                visited.add((x, y, dir))
                y += 1
            x, y = original_x, original_y
            while (x, y, dir) in sides:
                visited.add((x, y, dir))
                y -= 1
        elif (dir == 'left' or dir == 'right'):
            x, y = original_x, original_y
            while (x, y, dir) in sides:
                # going right
                visited.add((x, y, dir))
                x += 1
            x, y = original_x, original_y
            while (x, y, dir) in sides:
                visited.add((x, y, dir))
                x -= 1

    return s


def solve() -> None:
    input = stdin.read().splitlines()
    visited = set()
    grid = [[y for y in x] for x in input]
    part_1, part_2 = 0, 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in visited:
                continue
            area = 1
            perimeter = 0
            sides = []
            type = grid[i][j]
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in dirs:
                    nx, ny = x + dx, y + dy
                    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]) or grid[nx][ny] != type:
                        perimeter += 1
                        dir = dirs_map[(dx, dy)]
                        sides.append((nx, ny, dir))
                        continue
                    if grid[nx][ny] == type and (nx, ny) not in visited:
                        area += 1
                        stack.append((nx, ny))
                        visited.add((nx, ny))
            part_1 += area*perimeter
            part_2 += area*number_of_sides(sides)

    print(part_1)
    print(part_2)


if __name__ == '__main__':
    solve()
