#!/usr/bin/python3
"""
Python script that,
using this REST API,
for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv


EMPLOYEE_ID = argv[1]
url = "https://jsonplaceholder.typicode.com/users/"


if __name__ == '__main__':
    """returns information about his/her TODO list progress"""
    res = requests.get(f"{url}{EMPLOYEE_ID}")
    response = requests.get(f"{url}{EMPLOYEE_ID}/todos")
    name = res.json()['name']
    done = 0
    total = 0
    TASK_TITLES = ''
    for todo in response.json():
        if todo['completed'] is True:
            TASK_TITLES += f"\t {todo['title']}\n"
            done += 1
        total += 1
    print(f"Employee {name} is done with tasks({done}/{total}):")
    print(TASK_TITLES, end='')
