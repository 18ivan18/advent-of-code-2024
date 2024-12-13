#!/opt/homebrew/bin/python3.11

from z3 import Solver, Int, sat
from sys import stdin

# A*94+B*22=8400
# A*34+B*67=5400


def solve() -> None:
    input = stdin.read().split('\n\n')
    part_1, part_2 = 0, 0
    for batch in input:
        button1, button2, prize = batch.split('\n')
        values1 = button1.split("Button A: ")
        x1, y1 = values1[1].split(", ")
        x1, y1 = int(x1.split("X+")[1]), int(y1.split("Y+")[1])
        values2 = button2.split("Button B: ")
        x2, y2 = values2[1].split(", ")
        x2, y2 = int(x2.split("X+")[1]), int(y2.split("Y+")[1])
        prizes = prize.split("Prize: ")
        prize_x, prize_y = prizes[1].split(", ")
        prize_x, prize_y = int(prize_x.split(
            "X=")[1]), int(prize_y.split("Y=")[1])
        tx1, ty1 = Int('times_x1'), Int('times_y1')

        solver = Solver()
        solver.add(tx1*x1+ty1*x2 == prize_x, tx1*y1+ty1 *
                   y2 == prize_y, tx1 < 100,  ty1 < 100)
        if solver.check() == sat:
            m = solver.model()
            part_1 += 3*int(m[tx1].as_string()) + int(m[ty1].as_string())

        prize_x_2 = prize_x+10000000000000
        prize_y_2 = prize_y+10000000000000

        tx2, ty2 = Int('times_x1'), Int('times_y1')
        solver = Solver()
        solver.add(tx2*x1+ty2*x2 == prize_x_2, tx2*y1+ty2*y2 == prize_y_2)
        if solver.check() == sat:
            m = solver.model()
            part_2 += 3*int(m[tx2].as_string()) + int(m[ty2].as_string())
    print(part_1)
    print(part_2)


if __name__ == '__main__':
    solve()
