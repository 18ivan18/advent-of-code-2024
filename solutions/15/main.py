#!/usr/bin/env python3

from sys import stdin

dirs = {'^': (-1, 0), 'v': (1, 0), '>': (0, 1), '<': (0, -1)}


def find_start(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '@':
                return i, j
    raise ValueError('Start not found')


def do_move(x, y, dx, dy, grid):
    nx, ny = x + dx, y + dy
    tile_value = grid[x][y]
    if nx < 0 or nx >= len(grid) or ny < 0 or ny >= len(grid[0]):
        return False, x, y
    if grid[nx][ny] == '#':
        return False, x, y
    if grid[nx][ny] == 'O':
        moved, _, _ = do_move(nx, ny, dx, dy, grid)
        if not moved:
            return False, x, y
    grid[x][y] = '.'
    grid[nx][ny] = tile_value
    return True, nx, ny


def print_map(grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            print(grid[i][j], end='')
        print()
    print()


def part_1(input):
    map, moves = input.split('\n\n')
    map = [[y for y in x] for x in map.split('\n')]
    x, y = find_start(map)
    for move in moves.replace('\n', ''):
        dx, dy = dirs[move]
        _, nx, ny = do_move(x, y, dx, dy, map)
        x, y = nx, ny
    part_1_res = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == 'O':
                part_1_res += 100*i + j
    return part_1_res


def can_move(x, y, move, grid):
    dx, dy = dirs[move]
    nx, ny = x + dx, y + dy
    if grid[nx][ny] == '#':
        return False
    if grid[nx][ny] == '.':
        return True
    if (grid[nx][ny] == ']' or grid[nx][ny] == '[') and (move == '<' or move == '>'):
        return can_move(nx, ny, move, grid)
    if grid[nx][ny] == ']' and (move == '^' or move == 'v'):
        moved1 = can_move(nx, ny, move, grid)
        moved2 = can_move(nx, ny-1, move, grid)
        return moved1 and moved2
    if grid[nx][ny] == '[' and (move == '^' or move == 'v'):
        moved1 = can_move(nx, ny, move, grid)
        moved2 = can_move(nx, ny+1, move, grid)
        return moved1 and moved2

    raise ValueError(f'Invalid move, {move} from {x}, {y}')


def do_move_part_2(x, y, move, grid):
    dx, dy = dirs[move]
    nx, ny = x + dx, y + dy
    tile_value = grid[x][y]
    if grid[nx][ny] == '#':
        return False, x, y
    if grid[nx][ny] == '.':
        grid[nx][ny] = tile_value
        grid[x][y] = '.'
        return True, nx, ny
    if (grid[nx][ny] == ']' or grid[nx][ny] == '[') and (move == '<' or move == '>'):
        can = can_move(nx, ny, move, grid)
        if not can:
            return False, x, y
        do_move_part_2(nx, ny, move, grid)
        grid[nx][ny] = tile_value
        grid[x][y] = '.'
        return True, nx, ny
    if grid[nx][ny] == ']' and (move == '^' or move == 'v'):
        moved1, moved2 = can_move(
            nx, ny, move, grid), can_move(nx, ny-1, move, grid)
        if not moved1 or not moved2:
            return False, x, y
        do_move_part_2(nx, ny, move, grid)
        do_move_part_2(nx, ny-1, move, grid)
        grid[nx][ny] = tile_value
        grid[nx][ny-1] = '.'
        grid[x][y] = '.'
        return True, nx, ny
    if grid[nx][ny] == '[' and (move == '^' or move == 'v'):
        moved1, moved2 = can_move(
            nx, ny, move, grid), can_move(nx, ny+1, move, grid)
        if not moved1 or not moved2:
            return False, x, y
        do_move_part_2(nx, ny, move, grid)
        do_move_part_2(nx, ny+1, move, grid)
        grid[nx][ny] = tile_value
        grid[nx][ny+1] = '.'
        grid[x][y] = '.'
        return True, nx, ny

    raise ValueError(f'Invalid move, {move} from {x}, {y}')


def part_2(input):
    map, moves = input.split('\n\n')
    map = [[y for y in x] for x in map.split('\n')]
    build_new_map = []
    for i in range(len(map)):
        row = []
        for j in range(len(map[i])):
            if map[i][j] == '#':
                row += '#'
                row += '#'
            if map[i][j] == 'O':
                row += '['
                row += ']'
            if map[i][j] == '.':
                row += '.'
                row += '.'
            if map[i][j] == '@':
                row.append('@')
                row.append('.')
        build_new_map.append(row)
    map = build_new_map
    x, y = find_start(map)
    # print_map(map)

    for move in moves.replace('\n', ''):
        _, nx, ny = do_move_part_2(x, y, move, map)
        # print(move, x, y)
        x, y = nx, ny
        # print_map(map)
    part_2_res = 0
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == '[' and map[i][j+1] == ']':
                part_2_res += 100*i + j
    return part_2_res


def solve() -> None:
    input = stdin.read()
    print(part_1(input))
    print(part_2(input))


if __name__ == '__main__':
    solve()
