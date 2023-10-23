#!/usr/bin/python3


"""
Module where the results of a todo list
are exported to a csv file.
"""

import csv
import requests
import sys  # alphabetical order


def main_func():
    """this is themain function"""
    user_id = int(sys.argv[1])  # second command line arg
    todo_url = 'https://jsonplaceholder.typicode.com/todos'
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    file_data = []

    retrivedlist = requests.get(todo_url)
    user_name = requests.get(user_url).json().get('username')

    for todo in retrivedlist.json():
        if todo.get('userId') == user_id:
            file_data.append(
                [str(user_id),
                 user_name,
                 todo.get('completed'),
                 "{}".format(todo.get('title'))])

    print(file_data)
    file_name = "{}.csv".format(user_id)
    with open(file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        for row in file_data:
            for item in row:
                str(item)
            csv_writer.writerow(row)
        print('file written successfully')


if __name__ == "__main__":
    main_func()
