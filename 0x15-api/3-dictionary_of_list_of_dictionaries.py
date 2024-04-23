#!/usr/bin/python3
""" Extend Python script to export data in the JSON format """
import json
import requests
import sys


if __name__ == "__main__":
    users = requests.get(f"https://jsonplaceholder.typicode.com/users")
    users = users.json()
    todo = requests.get(f"https://jsonplaceholder.typicode.com/todos")
    todoj = todo.json()
    dic = {}
    for user in users:
        lis = []
        for task in todoj:
            if task.get('userId') == user.get('id'):
                task_dic = {"task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": user.get('username')}
                lis.append(task_dic)
        dic[user.get('id')] = lis
    with open('todo_all_employees.json', 'w') as file:
        json.dump(dic, file)
