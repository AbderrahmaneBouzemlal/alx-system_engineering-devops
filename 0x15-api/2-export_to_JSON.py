#!/usr/bin/python3
"""
Python script that,
using this REST API,
for a given employee ID,
and export it as a json file.
"""
import json
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
    data = []
    for todo in response.json():
        del todo["id"]
        todo['username'] = username
        todo['task'] = todo['title']
        del todo['title']
        del todo['userId']
        data.append(todo)
    json_obj = {EMPLOYEE_ID: data}
    with open(f"{EMPLOYEE_ID}.json", 'w') as jsonfile:
        json.dump(json_obj, jsonfile)
