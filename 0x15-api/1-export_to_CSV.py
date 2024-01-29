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

    with open("{}.csv".format(ids), 'w', newline='') as csvfile:
        tasks = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for tsk in todo:
            tasks.writerow([int(ids), user.get('username'),
                            tsk.get('completed'), tsk.get('title')])
