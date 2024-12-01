#!/usr/bin/env python3

import os
from base import solutions_dir, day_str, path

with open(os.path.join(solutions_dir, day_str, 'README.md')) as f:
    problem_name = f.readline()[6:-5]

with open(os.path.join(path, 'README.md'), 'r+') as readme:
    input = readme.read()
    if problem_name not in input:
        readme.write(f"- [{problem_name}](./solutions/{day_str})\n")
    else:
        print(f"{problem_name} already added to README.md")
