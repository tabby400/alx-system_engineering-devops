#!/usr/bin/python3
"""
this used to get the tasks done by an employee
through an API and employee id as input
"""

import requests
import sys  # organized alphabetically


def main_func():
    """this is the function"""

    user_id = int(sys.argv[1])  # second command line arg
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    retrivedlist = requests.get(todo_url)

    all_asked = 0
    completed = []
    for todo in retrivedlist.json():

        if todo['userId'] == user_id:
            all_asked = all_asked + 1

            if todo['completed']:
                completed.append(todo['title'])

    user_name = requests.get(user_url).json()['name']

    printer = ("Employee {} is done with tasks({}/{}):".format(user_name,
               len(completed), all_asked))
    print(printer)
    for p in completed:
        print("\t {}".format(p))  # one tabulation and one space


if __name__ == '__main__':
    main_func()
