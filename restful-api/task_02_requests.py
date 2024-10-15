#!/usr/bin/python3


"""
Import necessary libraries
"""


import requests
import csv
import json

def fetch_and_print_posts():

    """
    Fetches posts from JSONPlaceholder and prints the titles of all posts.
    """

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        postslist = r.json()
    print("Status Code: {}" .format(r.status_code))
    for posts in postslist:
        print(posts['title'])
def fetch_and_save_posts():

    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """
    info = ""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        info = r.json()
    data = []
    for i in info:
        data.append({
            'id' : i['id'] ,
            'title' : i['title'],
            'body' : i['body']
        })
    with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        writer.writerows(data)
