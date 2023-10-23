#!/usr/bin/python3

"""
Module
This is all about exporting datat in json
format
"""

import json
import requests
import sys  # import  in alphabetical order


def main_func():
    """the main function"""
    user_id = int(sys.argv[1])
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    retrivedlist = requests.get(todo_url)
    user_name = requests.get(user_url).json().get('username')
    user_data = []
    result = {user_id: user_data}

    for todo in retrivedlist.json():
        if todo.get('userId') == user_id:
            user_data.append(
                {
                    "task": todo.get('title'),
                    "completed": todo.get('completed'),
                    "username": user_name,
                })
    print(result)
    file_name = "{}.json".format(user_id)
    with open(file_name, 'w') as file:
        json.dump(result, file)


if __name__ == '__main__':  # executed directly
    main_func()
