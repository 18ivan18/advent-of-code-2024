#!/usr/bin/env python3

from sys import stdin

operators_1 = ['+', '*']
operators_2 = ['+', '*', '|']


def eval_left_to_right(values: str, operators: list[str]):
    res = 0
    operator = '+'
    val = 0
    values += ' '
    for c in values:
        if c.isnumeric():
            val = val*10+int(c)
        if c in operators or c == ' ':
            if operator == '+':
                res += val
            elif operator == '*':
                res *= val
            elif operator == '|':
                res = int(str(res) + str(val))
            operator = c
            val = 0

    return res


def possible_to_calculate(values: str, target: int, operators: list[str]):
    if values.count(' ') == 0:
        return target if eval_left_to_right(values, operators) == target else 0
    for op in operators:
        nvalues = values.replace(' ', op, 1)
        if possible_to_calculate(nvalues, target, operators):
            return target
    return 0

# runs 45 secs


def solve() -> None:
    input = stdin.read().splitlines()
    print(sum([possible_to_calculate(line.split(': ')[1],
          int(line.split(': ')[0]), operators_1) for line in input]))
    print(sum([possible_to_calculate(line.split(': ')[1],
          int(line.split(': ')[0]), operators_2) for line in input]))


if __name__ == '__main__':
    solve()
