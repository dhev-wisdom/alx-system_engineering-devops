#!/usr/bin/python3
"""
Python script should export data in the CSV format
"""

import csv
import requests
import sys


def export_csv():
    """
    Module exports file in csv format
    """

    id_ = sys.argv[1]
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(id_))
    todos = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos/"
                         .format(id_))
    user_data = user.json()
    todo_data = todos.json()
    user_name = user_data["name"]
    data = []
    for i in range(len(todo_data)):
        single_data = []
        status = todo_data[i]["completed"]
        title = todo_data[i]["title"]
        sentence = [id_, user_name, status, title]
        data.append(sentence)
    file_name = id_ + ".csv"
    with open(file_name, "w") as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for row in data:
            writer.writerow(row)


if __name__ == "__main__":
    export_csv()
