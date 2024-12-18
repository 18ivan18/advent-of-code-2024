#!/usr/bin/env python3

from sys import stdin

# max = 7
max = 71
# part_1_simulation_max = 11
part_1_simulation_max = 1023


def solve() -> None:
    input = stdin.read().splitlines()
    grid = [['.' for _ in range(max)] for _ in range(max)]
    i = 0
    for line in input:
        p = False
        if i == part_1_simulation_max:
            p = True
        start_x, start_y = line.split(',')
        grid[int(start_x)][int(start_y)] = '#'
        i += 1
        queue = [(0, 0, 0)]
        visited = set()
        path_found = False
        while queue:
            x, y, steps = queue.pop(0)
            if x == max-1 and y == max-1:
                if p:
                    print(steps)
                path_found = True
                break
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nx, ny = x + dx, y + dy
                if nx < 0 or nx >= max or ny < 0 or ny >= max:
                    continue
                if grid[nx][ny] == '#':
                    continue
                if (nx, ny) in visited:
                    continue
                visited.add((nx, ny))
                queue.append((nx, ny, steps + 1))
        if not path_found:
            print(f"{start_x}, {start_y}")
            break


if __name__ == '__main__':
    solve()
