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
    array_ = []
    id_ = sys.argv[1]

    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id_)).json()
    todo = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                        .format(id_)).json()
    username = user["name"]

    for i in range(len(todo)):
        dict_ = {"task": todo[i]["title"], "completed": todo[i]["completed"],
                 "username": username}
        array_.append(dict_)

    employee_dict[id_] = array_

    filename = id_ + ".json"

    with open(filename, "w") as file:
        json.dump(employee_dict, file)


if __name__ == "__main__":
    export_json()
