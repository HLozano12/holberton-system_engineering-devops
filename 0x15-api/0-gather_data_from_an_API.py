#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,"""
import requests
from sys import argv


if __name__ == "__main__":

    count = 0
    task_list = []

    # Get the request from site
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(arg[1]))
    todo = requests.get('https://jsonplaceholder.typicode.com/users/{}/todos'
                        .format(argv[1]))

    # obtain information from the json response
    name = user.json().get('name')
    task = todo.jason()

    for task in task:
        if task.get('completed') is True:
            count += 1
            task_list.append(task.get('title'))

    # Print out the first line
    print('Employee {} is done with tasks({}/{}):'
          .format(name, count, len(task)))

    for task in task_list:
        print('\t {}'.format(task))
