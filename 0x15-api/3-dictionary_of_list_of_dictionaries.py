#!/usr/bin/python3
'''api response json'''
import csv
import requests
import sys
import json

if __name__ == '__main__':
    url = 'https://jsonplaceholder.typicode.com/'
    todo = requests.get(url + 'todos').json()
    user = requests.get(url + 'users').json()

    usrd = {}
    usrndict = {}
    for users in user:
        ids = users.get("id")
        usrd[ids] = []
        usrndict[ids] = users.get("username")

    for task in todo:
        tskd = {}
        ids = task.get("userId")
        tskd["username"] = usrndict.get(ids)
        tskd["task"] = task.get('title')
        tskd["completed"] = task.get('completed')
        usrd.get(ids).append(tskd)
    with open("todo_all_employees.json", 'w') as jsn:
        json.dump(usrd, jsn)
