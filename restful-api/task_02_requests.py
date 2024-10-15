#!/usr/bin/python3


"""
Import necessary libraries
"""


import requests
import csv


def fetch_and_print_posts():

    """
    Fetches posts from JSONPlaceholder and prints the titles of all posts.
    """

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = r.json()
    for posts in posts:
        print(posts['title'])
def fetch_and_save_posts():

    """
    Fetches posts from JSONPlaceholder and saves them to a CSV file.
    """

    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        posts = r.json()
    data = []
    for posts in posts:
        data.append({
            'id' : posts['id'],
            'title' : posts['title'],
            'body' : posts['body']
        })
    with open('posts.csv', mode='w', newline='', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=['id', 'title', 'body'])
        writer.writeheader
        writer.writerows(data)
fetch_and_print_posts()
fetch_and_save_posts()
