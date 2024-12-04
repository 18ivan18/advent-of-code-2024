#!/usr/bin/env python3

from sys import stdin

xmas_search = ['XMAS', 'SAMX']


def get_number_of_xmas(i: int, j: int, grid: list[list[str]]) -> int:
    # get all words starting from i j going in all directions
    words = [(grid[i][j], i, j) for _ in range(8)]
    for k in range(3):
        for indx, (dx, dy) in enumerate([(1, 0), (1, 1), (1, -1), (0, 1), (-1, 1), (-1, -1), (-1, 0), (0, -1)]):
            w, x, y = words[indx]
            x += dx
            y += dy
            if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
                continue
            w += grid[x][y]
            words[indx] = (w, x, y)

    return sum([1 for word in words if word[0] in xmas_search])


x_max_search = ['MAS', 'SAM']


def is_x_mas(grid: list[list[str]], i: int, j: int) -> int:
    # get diagonal words of length 3
    if i - 1 < 0 or i + 1 >= len(grid) or j - 1 < 0 or j + 1 >= len(grid[0]):
        return 0
    left_to_right = grid[i - 1][j - 1] + grid[i][j] + grid[i + 1][j + 1]
    right_to_left = grid[i - 1][j + 1] + grid[i][j] + grid[i + 1][j - 1]
    return 1 if left_to_right in x_max_search and right_to_left in x_max_search else 0


def get_number_of_x_mas(grid: list[list[str]]) -> int:
    c = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'A':
                c += is_x_mas(grid, i, j)
    return c


def solve() -> None:
    input = [[y for y in x] for x in stdin.read().splitlines()]
    print(sum([get_number_of_xmas(i, j, input)
          for i in range(len(input)) for j in range(len(input[0]))])/2)
    print(get_number_of_x_mas(input))


if __name__ == '__main__':
    solve()
