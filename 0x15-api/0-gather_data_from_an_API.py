#!/usr/bin/python3
"""

"""
import requests
from sys import argv


argc = len(argv)
EMPLOYEE_ID = argv[1]


def main():
    """returns information about his/her TODO list progress"""
    res = requests.get(f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}")
    response = requests.get(f"https://jsonplaceholder.typicode.com/users/{EMPLOYEE_ID}/todos")
    EMPLOYEE_NAME = res.json()['name']
    NUMBER_OF_DONE_TASKS = 0
    TOTAL_NUMBER_OF_TASKS = 0
    TASK_TITLES = ''
    for todo in response.json():
        if todo['completed'] == True:
            TASK_TITLES += f"\t {todo['title']}\n"
            NUMBER_OF_DONE_TASKS += 1
        TOTAL_NUMBER_OF_TASKS += 1
    print(f"Employee {EMPLOYEE_NAME} is done with tasks({NUMBER_OF_DONE_TASKS}/{TOTAL_NUMBER_OF_TASKS}):")
    print(TASK_TITLES, end='')


if __name__ == '__main__':
    main()
