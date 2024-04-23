#!/usr/bin/python3
""" extend Python script to export data in the CSV format """
import csv
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    name = user.json().get('name')
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    todoj = todo.json()

    filename = f"{userId}.csv"
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_MINIMAL)
        for task in todoj:
            if task.get('userId') == int(userId):
                a = task.get('completed')
                b = task.get('title')
                out = f'"{userId}","{name}","{a}","{b}"'
                # print(out)
                writer.writerow([userId, name, a, b])
