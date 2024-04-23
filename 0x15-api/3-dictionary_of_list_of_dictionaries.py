#!/usr/bin/python3
"""Extend Python script to export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    # Fetching users and todos data from the API
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    
    # Dictionary to store all tasks
    todo_all = {}

    # Iterating through users
    for user in users:
        task_list = []
        # Iterating through todos
        for task in todos:
            if task.get('userId') == user.get('id'):
                task_dict = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user.get('username')
                }
                task_list.append(task_dict)
        todo_all[user.get('id')] = task_list

    # Writing the data to JSON file
    with open('todo_all_employees.json', mode='w') as f:
        json.dump(todo_all, f)
