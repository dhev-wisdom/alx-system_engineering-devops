#!/usr/bin/python3
"""
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""

import requests
import sys

if __name__ == "__main__":
    id_ = sys.argv[1]

    users = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                         .format(id_))
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos"
                         .format(id_))
    data1 = users.json()
    data2 = todos.json()
    completed_tasks = 0
    complete_tasks = []
    total_tasks = 0
    employee_name = data1["name"]
    for i in range(len(data2)):
        if data2[i]["completed"] is False:
            completed_tasks += 1
            complete_tasks.append(data2[i]["title"])
        total_tasks += 1
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed_tasks, total_tasks))
    for i in complete_tasks:
        print("\t", i)
