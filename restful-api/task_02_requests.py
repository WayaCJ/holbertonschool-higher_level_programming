#!/usr/bin/python3

import requests
import csv

"""module for two functions"""


def fetch_and_print_posts():

    """Fetches posts from jsonplaceholder and prints status code
    if successful, parses fetched date into json object"""

    url = 'https://jsonplaceholder.typicode.com/posts'

    r = requests.get(url)

    print("Status Code:", r.status_code)

    if r.status_code == 200:

        posts = r.json()

    for post in posts:
        print("Title: ", post['title'])

    else:
        print("Error: ", r.status_code)

def fetch_and_save_posts():

    """fetches post from jsonplaceholder and saves them into csv file"""

    url = 'https://jsonplaceholder.typicode.com/posts'

    r = requests.get(url)

    if r.status_code == 200:
       
        posts = r.json()

        s_posts = []
        for post in posts:
            s_post = {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            s_posts.append(s_post)

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            writer.writeheader()
            for post in s_posts:
                writer.writerow(post)
    else:
        print("Error:", r.status_code)

if __name__ == "__main__":
    fetch_and_print_posts()
    fetch_and_save_posts()
