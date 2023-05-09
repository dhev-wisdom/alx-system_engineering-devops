#!/usr/bin/python3
"""
Python script to export data in the JSON format.
"""

import json
import requests
import sys


def export_json():
    """
    Module export data to json file
    """
    employee_dict = {}

    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    i = 1

    for user in users:
        """
        Helper function to create data to be exported
        """
        array_ = []
        todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/".format(i)).json()

        username = user["name"]

        for a in range(len(todo)):
            title = todo[a]["title"]
            status = todo[a]["completed"]
            dict_ = {"username": username, "task": title, "completed": status}
            array_.append(dict_)

        employee_dict[i] = array_
        i += 1

    with open("todo_all_employees.json", "w") as file:
        json.dump(employee_dict, file)


if __name__ == "__main__":
    export_json()
