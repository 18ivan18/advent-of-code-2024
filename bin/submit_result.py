#!/usr/bin/env python3

import requests
from base import bcolors, session_cookie, advent_of_code_base_url, year, day, level
from get_answer import get_answer

# Submit the solution
answer = get_answer(day, level)
url = f'{advent_of_code_base_url}/{year}/day/{day}/answer'
data = {'level': level, 'answer': answer}

headers = {'cookie': f'session={session_cookie}'}

print(f"Submitting {day=} {level=} {answer=}")
response = requests.post(url, data=data, headers=headers, allow_redirects=True)

if response.text.find("Did you already complete it") != -1:
    print(f"{bcolors.BOLD}{day=} {level=} is already completed.{bcolors.ENDC}")

if response.text.find("not the right answer") != -1:
    print(f"{bcolors.FAIL}{day=} {level=} Wrong Answer.{bcolors.ENDC}")

if response.text.find("too recently") != -1:
    print(f"{bcolors.FAIL}Submitted too recently.{bcolors.ENDC}")

if response.text.find("That's the right answer") != -1:
    print(f"{bcolors.OKGREEN}Correct answer. Getting part 2.{bcolors.ENDC}")
