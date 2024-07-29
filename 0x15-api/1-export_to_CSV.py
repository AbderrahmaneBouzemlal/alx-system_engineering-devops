#!/usr/bin/python3
"""
Python script that,
using this REST API,
for a given employee ID,
and export it as a csv file.
"""
import csv
import requests
import sys


url = "https://jsonplaceholder.typicode.com/users/"


if __name__ == '__main__':
    """returns information about his/her TODO list progress"""
    if len(sys.argv) < 2:
        sys.exit()
    EMPLOYEE_ID = sys.argv[1]
    username = requests.get(f"{url}{EMPLOYEE_ID}").json()['username']
    response = requests.get(f"{url}{EMPLOYEE_ID}/todos")
    field_names = ["userId", "username", "completed", "title"]
    data = []
    for todo in response.json():
        del todo["id"]
        todo['username'] = username
        data.append(todo)
    with open(f"{EMPLOYEE_ID}.csv", 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=field_names)
        writer.writerows(data)
