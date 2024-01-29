#!/usr/bin/python3
'''api response json'''
import csv
import requests
import sys
import json


if __name__ == '__main__':
    ids = sys.argv[1]

    url = 'https://jsonplaceholder.typicode.com/'
    todo = requests.get(url + 'todos?userId={}'.
                        format(ids)).json()
    user = requests.get(url + 'users/{}'.format(ids)).json()
    tsks = []
    js = {}
    for task in todo:
        tskj = {}
        tskj["task"] = task.get('title')
        tskj["completed"] = task.get('completed')
        tskj["username"] = user.get('username')
        tsks.append(tskj)
    js[ids] = tsks
    with open("{}.json".format(ids), 'w') as jsn:
        json.dump(js, jsn)
