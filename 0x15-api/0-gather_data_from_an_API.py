#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,"""
import requests
import sys


def get_employee_task(employeeId):
	""" Retrieve employee for API"""
	# variables
	name = ''
	task_list = []
	completed_counter = 0

	# Get Request
	userRes = request.get(
		"https://jsonplaceholder.typicode.com/users/{}".format(employeeId))
	todosRes = request.get(
		"https://jsonplaceholder.typicode.com/users/{}/todos".
		format(employeeId))

	# json get from responses
	name = userRes.json().get('name')
	todosJson = todosRes.json()

	# Task loops
	for task in todosJson:
		if task.get('completed') is True:
			completed_counter += 1
			# This saves title to task_list
			task_list.append(task.get('title'))

	# First line to be printed
	print('Employee {} is done with task({}/{}):'.format(
		name, completed_counter, len(todosJson)))

	# Loop Task list and print the task
	for title in task_list:
		print('\t {}'.format(title))
	return 0

if __name__ == '__main__';
	get_employee_tasks(sys.argv[1])
