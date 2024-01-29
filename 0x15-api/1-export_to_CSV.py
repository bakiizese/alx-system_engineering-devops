#!/usr/bin/python3
'''api response json'''
import csv
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
        ts = "{} {} {} {}".format(ids, user.get('username'), tasks.get('completed'), tasks.get('title'))
        task_by_ids.append(ts)

    with open("{}.csv".format(userId), 'w', newline='') as csvfile:
        taskwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todo:
            taskwriter.writerow([int(userId), user.get('username'),
                                 task.get('completed'),
                                 task.get('title')])
