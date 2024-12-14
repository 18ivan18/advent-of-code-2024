#!/usr/bin/env python3

from sys import stdin

# top left is 0,0
# negative y is down
# wrap around the wall

max_x, max_y = 101, 103
# max_x, max_y = 11, 7
q1 = (0, int(max_x/2), 0, int(max_y/2))
q2 = (int(max_x/2)+1, max_x, 0, int(max_y/2))
q3 = (int(max_x/2)+1, max_x, int(max_y/2)+1, max_y)
q4 = (0, int(max_x/2), int(max_y/2)+1, max_y)
quadrants = [q1, q2, q3, q4]


def move_once(x, y, vel_x, vel_y):
    x = (x + vel_x) % max_x
    y = (y + vel_y) % max_y
    return x, y


def move(x, y, vel_x, vel_y, secs=100):
    for _ in range(secs):
        x, y = move_once(x, y, vel_x, vel_y)
    for i, (min_qx, max_qx, min_qy, max_qy) in enumerate(quadrants):
        if x >= min_qx and x < max_qx and y >= min_qy and y < max_qy:
            return i
    return -1


def pretty_print(grid):
    for line in grid:
        print(line)


def solve() -> None:
    input = stdin.read().splitlines()
    q = {0: 0, 1: 0, 2: 0, 3: 0, -1: 0}
    for line in input:
        starting_pos, velocities = line.split(' ')
        x, y = [int(a) for a in starting_pos.split('p=')[1].split(',')]
        vel_x, vel_y = [int(a) for a in velocities.split('v=')[1].split(',')]
        quadrant = move(x, y, vel_x, vel_y)
        q[quadrant] += 1
    print(q[0]*q[1]*q[2]*q[3])
    robots = []
    for line in input:
        starting_pos, velocities = line.split(' ')
        x, y = [int(a) for a in starting_pos.split('p=')[1].split(',')]
        vel_x, vel_y = [int(a) for a in velocities.split('v=')[1].split(',')]
        robots.append((x, y, vel_x, vel_y))
    for j in range(6600):
        grid = [['.' for _ in range(max_x)] for _ in range(max_y)]
        for i, (x, y, vel_x, vel_y) in enumerate(robots):
            x, y = move_once(x, y, vel_x, vel_y)
            grid[y][x] = '#'
            robots[i] = (x, y, vel_x, vel_y)
        if j > 6500:
            pretty_print(grid)
            print(j, sep='\n')


if __name__ == '__main__':
    solve()
