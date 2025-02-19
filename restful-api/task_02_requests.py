#!/usr/bin/python3
'''
In this module we are interacting
with a public API
'''


import requests
import json
import csv


def fetch_and_print_posts():
    '''
    Function to print all the posts
    in json
    '''
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        info = r.json()
        print("Status Code: {}".format(r.status_code))
    for posts in info:
        print(posts['title'])


def fetch_and_save_posts():
    '''
    Function to fetch posts and save it
    in a csv file
    '''
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        info = r.json()
    data = []
    for i in info:
        data.append({
            'id': i['id'],
            'body': i['body'],
            'title': i['title'],
        })
    with open('posts.csv', 'w', newline='', encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(data)
