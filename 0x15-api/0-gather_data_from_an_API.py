#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID"""
import requests
import sys

if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    name = user.json().get('name')
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    todoj = todo.json()
    complete = 0
    alltasks = 0
    tasks = []
    for task in todoj:
        if task.get('userId') == int(userId):
            alltasks += 1
            if task.get('completed'):
                complete += 1
                tasks.append(task.get('title'))

    print(f"Employee {name} is done with tasks({complete}/{alltasks}):")
    for task in tasks:
        print(f"\t {task}")
