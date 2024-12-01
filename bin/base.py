import json
from pathlib import Path
import os
import sys

advent_of_code_base_url = 'https://adventofcode.com'
path = Path(__file__).parents[1]
solutions_dir = os.path.join(path, 'solutions')


def today() -> int:
    days = [int(x) for x in os.listdir(solutions_dir)]
    days.append(0)
    return sorted(days)[-1]


env_path = os.path.join(path, '.env')
env_sample_path = os.path.join(path, '.env.sample')
env = json.load(open(env_path if os.path.exists(
    env_path) else env_sample_path))
session_cookie = env['session']
year = env['year']
day = int(sys.argv[1]) if len(sys.argv) > 1 else today()
level = int(sys.argv[2]) if len(sys.argv) > 2 else 1
day_str = f"{day:02}"


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
