#!/usr/bin/python3
"""
    Module 0-gather_data_from_an_API
"""
import requests
from pprint import pprint
from sys import argv

if __name__ == '__main__':

    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}/todos')
    completed = []
    for todo_item in resp.json():
        if todo_item['completed'] == True:
            completed.append(todo_item['title'])
    total_tasks = len(resp.json())
    completed_tasks = len(completed)
    resp = requests.get(f'https://jsonplaceholder.typicode.com/users/{argv[1]}')
    user_name = resp.json().get('name')

    print(f'Employee {user_name} is done with tasks ({completed_tasks}/{total_tasks}):')
    for task in completed:
        print(f'\t {task}')
