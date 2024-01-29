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

    print(task_by_ids)
    with open('{}.csv'.format(ids), mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=' ')
        csv_writer.writerows(task_by_ids)

