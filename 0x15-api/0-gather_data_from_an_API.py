#!/usr/bin/python3
'''api response json'''
import requests
import sys


if __name__ == '__main__':
    ids = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    todo = requests.get(url + 'todos').json()
    user = requests.get(url + 'users').json()

    task_by_ids = []
    tot = 0
    name = None
    for tasks in todo:
        if tasks['userId'] == int(ids):
            tot += 1
            if tasks['completed'] is True:
                task_by_ids.append(tasks['title'])
    for u in user:
        if u['id'] == int(ids):
            name = u['name']
    print("Employee {} is done with tasks({}/{}): "
          .format(name, len(task_by_ids), tot))
    for tsk in task_by_ids:
        print("\t{}".format(str(tsk)))
