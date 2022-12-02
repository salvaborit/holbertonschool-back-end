#!/usr/bin/python3
"""
Module 2-export_to_json
"""
from json import dump
import requests
from sys import argv

from pprint import pprint


if __name__ == '__main__':

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    username = resp.json().get('username')

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    task_list = []
    for task in resp.json():
        task_dict = {}
        task_dict['task'] = task['title']
        task_dict['completed'] = 'true' if task['completed'] else 'false'
        task_dict['username'] = username
        task_list.append(task_dict)

    final_dict = {}
    final_dict['2'] = task_list

    with open(argv[1] + '.json', 'w') as file:
        dump(final_dict, file)
