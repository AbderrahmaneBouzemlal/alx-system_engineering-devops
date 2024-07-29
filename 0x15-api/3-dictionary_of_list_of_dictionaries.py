#!/usr/bin/python3
"""
Python script that,
using this REST API,
for all employees,
and export it as a json file.
"""
import json
import requests


url = "https://jsonplaceholder.typicode.com/users/"


def exportall():
    """returns information about his/her TODO list progress"""
    usernames = {}
    all_employees = requests.get(f"{url}").json()
    for employee in all_employees:
        export(employee.get('id'), employee.get('username'))


def export(EMPLOYEE_ID, username):
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
    with open("todo_all_employees.json", 'a') as jsonfile:
        json.dump(json_obj, jsonfile)


if __name__ == '__main__':
    exportall()
