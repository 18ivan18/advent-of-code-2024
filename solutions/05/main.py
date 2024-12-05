#!/usr/bin/env python3

from collections import defaultdict
from sys import stdin


def is_correct(message, rules):
    s = set(message)
    for x in reversed(message):
        s.remove(x)
        if x not in rules:
            continue
        if len((set(rules[x]) & s)) > 0:
            return False
    return True


def correct(message, rules):
    while True:
        s = set(message)
        for x in reversed(message):
            s.remove(x)
            if x not in rules:
                continue
            if len((set(rules[x]) & s)) > 0:
                to_swap = (set(rules[x]) & s).pop()
                i_swap, x_idx = message.index(
                    to_swap), message.index(
                    x)
                message[i_swap], message[x_idx] = message[x_idx], message[i_swap]

                break
        if len(s) == 0:
            break
    return message[len(message) // 2]


def solve() -> None:
    input = stdin.read().splitlines()
    rules = defaultdict(list)
    for x in input[:input.index('')]:
        rules[int(x.split('|')[0])].append(int(x.split('|')[1]))
    messages = [x for x in input[input.index('') + 1:]]
    sum_correct, sum_incorrect = 0, 0
    for message in messages:
        message = [int(x) for x in message.split(',')]
        if is_correct(message, rules):
            sum_correct += message[len(message) // 2]
        else:
            sum_incorrect += correct(message, rules)
    print(sum_correct)
    print(sum_incorrect)


if __name__ == '__main__':
    solve()
