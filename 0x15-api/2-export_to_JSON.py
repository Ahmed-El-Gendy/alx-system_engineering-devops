#!/usr/bin/python3
""" extend Python script to export data in the CSV format """
import csv
import json
import requests
import sys


if __name__ == "__main__":
    userId = sys.argv[1]
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{userId}")
    name = user.json().get('username')
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    todoj = todo.json()
    dic = {}
    lis = []
    for task in todoj:
        task_dic = {"task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": name}
        lis.append(task_dic)
    dic[userId] = lis
    filename = f"{userId}.json"
    with open(filename, 'w') as file:
        json.dump(dic, file)
