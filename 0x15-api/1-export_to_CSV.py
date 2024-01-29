#!/usr/bin/python3
'''api response json'''
import requests
import sys


if __name__ == '__main__':
    ids = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    todo = requests.get(url + 'todos?userId={}'.
                        format(ids)).json()
    user = requests.get(url + 'users/{}'.format(ids)).json()

    task_by_ids = []
    for tasks in todo:
        ts = "{}","{}","{}","{}".format(ids, user.get('name'), tasks.get('conpleted'), tasks.get('title'))
        task_by_ids.append(ts)
    
    for i in task_by_ids:
        print(i)
