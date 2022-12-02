#!/usr/bin/python3
"""
Module 1-export_to_csv
"""
import requests
from sys import argv
import csv

from pprint import pprint


if __name__ == '__main__':

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(argv[1]))
    user_name = resp.json().get('name')

    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(argv[1]))

    with open('USER_ID.csv', 'w') as file:
        for todo_item in resp.json():
            writer = csv.writer(file)
            writer.writerow([str(todo_item['userId']),
                             str(user_name.split()[0]),
                             str(todo_item['completed']),
                             str(todo_item['title'])])
