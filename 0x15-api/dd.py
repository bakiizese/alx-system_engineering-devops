#!/usr/bin/python3
'''api response json'''
import requests
import sys


if __name__ == '__main__':
    ids = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    todo = requests.get(url + 'todos?userId={}'. format(ids), verify=False).json()
    user = requests.get(url + 'users/{}'.format(ids), verify=False).json()

    task_by_ids = []
    for tasks in todo:
        if tasks.get('completed') is True:
            task_by_ids.append(tasks.get('title'))
    print("Employee {} is done with tasks({}/{}):"
          .format(user.get('name'), len(task_by_ids), len(todo)))

    print("\n".join("\t {}".format(tsk) for tsk in task_by_ids))
