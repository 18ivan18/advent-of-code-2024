#!/usr/bin/env python3

from sys import stdin
import re


mul_regex = r"mul\((\d{1,3}),(\d{1,3})\)"
mul_with_conditions_regex = r"mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\)"


def solve() -> None:
    input = stdin.read()
    matches_mul = re.findall(mul_regex, input)
    print(sum([int(x) * int(y) for x, y in matches_mul]))

    matches = re.finditer(mul_with_conditions_regex, input)
    match_result_with_condition = 0
    do = True
    for match in matches:
        if match.group() == 'do()':
            do = True
        elif match.group() == "don't()":
            do = False
        elif do:
            match_result_with_condition += int(match.group(1)) * \
                int(match.group(2))

    print(match_result_with_condition)


if __name__ == '__main__':
    solve()
