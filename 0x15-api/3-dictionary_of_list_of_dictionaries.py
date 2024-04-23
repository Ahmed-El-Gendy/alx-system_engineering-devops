#!/usr/bin/python3
""" Extend Python script to export data in the JSON format """
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    
    todo_all = {}

    for user in users:
        task_list = []
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {
                    "username": user.get('username'),
                    "task": task.get('title'),
                    "completed": task.get('completed')
                }
                task_list.append(task_dict)
        todo_all[user.get('id')] = task_list
    
    with open('todo_all_employees.json', 'w') as file:
        json.dump(todo_all, file)
