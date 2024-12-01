#!/usr/bin/env python3

from base import solutions_dir, path, day, level

import argparse
import subprocess
import os


def get_answer(day: int, level: int, input: str = 'input.txt'):
    # Assuming your Python script is in the 'solutions' directory and follows a naming convention like 'day_01.py'
    script_path = os.path.join(solutions_dir, f"{day:02}")

    # Check if the script file exists
    if not os.path.exists(solutions_dir):
        print(f"Error: Solution script for day {day} not found.")

    # Execute the Python script using subprocess
    command = [os.path.join(path, 'bin', 'run.sh'),
               f"-d{script_path}", f"-i{input}"]
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    # Wait for the process to complete
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        # Successfully executed
        return stdout.splitlines()[level - 1]
    else:
        # An error occurred
        print(f"Error: Execution failed for day {day}, level {level}.")
        print("Error output:", stderr)
        return None


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Run the main.py script with optional input file argument.")
    parser.add_argument("-i", "--input_file", default="input.txt",
                        help="Specify the input file. Default is 'input.txt'.")
    parser.add_argument("-d", "--day", default=day,
                        help="Specify the day. Default is today.")
    parser.add_argument("-l", "--level", default=1,
                        help="Specify the puzzle level. Only 1 and 2 are accepted. Default is 1")
    args = parser.parse_args()

    print(get_answer(args.day, args.level, args.input_file))
