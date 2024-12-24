#!/usr/bin/env python3

from sys import stdin


def eval(a, op, b):
    if op == 'AND':
        return a & b
    elif op == 'OR':
        return a | b
    elif op == 'XOR':
        return a ^ b
    raise ValueError(f'Unknown operation {op}')


def part_1(initial_values, ops):
    values = {}
    for value in initial_values.splitlines():
        values[value.split(': ')[0]] = int(value.split(' ')[1])
    ops = ops.splitlines()
    while ops:
        operation = ops.pop(0)
        operands, result = operation.split(' -> ')
        op1, operand, op2 = operands.split(' ')
        if op1 not in values or op2 not in values:
            ops += [operation]
            continue
        values[result] = eval(
            values[op1], operand, values[op2])
    b, res = 0, ''
    while "z{:02d}".format(b) in values:
        res = str(values["z{:02d}".format(b)]) + res
        b += 1
    return int(res, 2)


def calculate(value_to_op, values, calc):
    print(calc)
    if calc in values:
        return values[calc]
    op1, operand, op2 = value_to_op[calc]
    first = calculate(value_to_op, values, op1)
    values[op1] = first
    second = calculate(value_to_op, values, op2)
    values[op2] = second
    res = eval(first, operand, second)
    values[calc] = res
    return res


def add(a, b, carry):
    res = a+b+carry
    return res % 2, res // 2


def part_2(initial_values, ops):
    values = {}
    for value in initial_values.splitlines():
        values[value.split(': ')[0]] = int(value.split(' ')[1])
    ops = ops.splitlines()
    value_to_op = {}
    for operation in ops:
        operands, result = operation.split(' -> ')
        op1, operand, op2 = operands.split(' ')
        value_to_op[result] = (op1, operand, op2)
    carry = 0
    for i in range(45):
        print(i)
        z_val = calculate(value_to_op, values, f"z{i:02d}")
        res, carry = add(values[f"x{i:02d}"], values[f"y{i:02d}"], carry)
        if res != z_val:
            raise ValueError(
                f"Expected z{i:02d} to be {res} but was {values[f'z{i:02d}']}")


def solve() -> None:
    initial_values, ops = stdin.read().split('\n\n')
    print(part_1(initial_values, ops))
    print(part_2(initial_values, ops))


if __name__ == '__main__':
    solve()
