#!/usr/bin/python3

"""
Here we are exporting data in json format
"""

import json
import requests
import sys  # alphabetically


if __name__ == "__main__":
    url = 'https://jsonplaceholder.typicode.com/'
    user = '{}users'.format(url)
    retrived = requests.get(user)
    json_o = retrived.json()
    taskdata = {}

    for user in json_o:
        name = user.get('username')
        userid = user.get('id')
        todos = '{}todos?userId={}'.format(url, userid)
        retrived = requests.get(todos)
        tasks = retrived.json()
        l_task = []
        for task in tasks:
            dic_task = {"username": name,
                        "task": task.get('title'),
                        "completed": task.get('completed')}
            l_task.append(dic_task)

        taskdata[str(userid)] = l_task
    filename = 'todo_all_employees.json'
    with open(filename, mode='w') as fh:
        json.dump(taskdata, fh)
