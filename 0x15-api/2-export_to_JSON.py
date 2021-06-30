#!/usr/bin/python3
"""for api"""
import json
import requests
import sys


def save_tasks_to_json(employeeId):
    """for api"""
    # variables
    username = ''
    userDict = {}

    # get requests
    usersRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".
        format(employeeId))
    todosRes = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".
        format(employeeId))

    # responses get from json
    username = usersRes.json().get('username')
    todosJson = todosRes.json()

    userDict[employeeId] = []
    # loop through and save info

    for task in todosJson:
        taskDict = {}
        taskDict['task'] = task.get('title')
        taskDict['username'] = username
        taskDict['completed'] = task.get('completed')

        userDict[employeeId].append(taskDict)

    with open("{}.json".format(employeeId), 'w') as jFile:
        json.dump(userDict, jFile)

if __name__ == '__main__':
    save_tasks_to_json(sys.argv[1])