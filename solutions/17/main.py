#!/usr/bin/env python3

from copy import deepcopy
from sys import stdin


part_1 = []


def map_combo_operands(x, registers):
    if x <= 3:
        return x
    return registers[x-4]


def adv(operand, registers, i):
    registers[0] = registers[0]//2**map_combo_operands(operand, registers)
    return i+2


def bxl(operand, registers, i):
    registers[1] = registers[1] ^ operand
    return i+2


def bst(operand, registers, i):
    registers[1] = map_combo_operands(operand, registers) % 8
    return i+2


def jnz(operand, registers, i):
    if registers[0] == 0:
        return i+2
    # literal operand
    return operand


def bxc(operand, registers, i):
    registers[1] = registers[1] ^ registers[2]
    return i+2


def out(operand, registers, i):
    global part_1
    part_1.append(f"{map_combo_operands(operand, registers) % 8}")
    return i+2


def bdv(operand, registers, i):
    registers[1] = registers[0]//2**map_combo_operands(operand, registers)
    return i+2


def cdv(operand, registers, i):
    registers[2] = registers[0]//2**map_combo_operands(operand, registers)
    return i+2


operands = {0: adv, 1: bxl, 2: bst, 3: jnz, 4: bxc, 5: out, 6: bdv, 7: cdv}


def run_program(program, registers):
    global part_1
    part_1 = []
    program, registers = deepcopy(program), deepcopy(registers)
    ip = 0
    while ip < len(program):
        ip = operands[program[ip]](
            program[ip+1], registers, ip)
    return ','.join(part_1)


def solve() -> None:
    registers, program = stdin.read().split('\n\n')
    program_string = program.split('Program: ')[1]
    program = [int(x) for x in program_string.split(',')]
    registers = [int(x.split(': ')[1]) for x in registers.split('\n')]
    print(run_program(program, registers))

    possibleA = [0]
    for _ in range(16):
        new_possibleA = []
        for a in possibleA:
            for remainder in range(8):
                new_possibleA.append(a*8+remainder)
        possibleA = new_possibleA
        new_possibleA = []
        for a in possibleA:
            b = a % 8 ^ 3
            c = a//(2**b)
            b ^= c
            b ^= 5
            out = b % 8
            if out == program[-1]:
                new_possibleA.append(a)
        program = program[:-1]
        possibleA = new_possibleA
    print(min(possibleA))


if __name__ == '__main__':
    solve()
