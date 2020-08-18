import argparse
import os
from collections import deque
import requests


def get_short_url(url):
    url = url.replace('https://', '')
    dot_position = url.rfind('.')
    return url if dot_position == -1 else url[:dot_position]


def is_url_correct(url, folder):
    return is_url_exist(url) or os.path.exists(folder + url)


def is_url_exist(url):
    if url.rfind('.') == -1:
        return False
    if not url.startswith('https://'):
        url = 'https://' + url
    return True if requests.get(url) else False


def print_tab(url, folder):
    with open(folder + get_short_url(url)) as tab:
        print(tab.read())


def save_tab(url, folder):
    if not is_url_exist(url):
        return
    if not url.startswith('https://'):
        url = 'https://' + url
    tab = requests.get(url)
    with open(folder + get_short_url(url), 'w') as file:
        file.write(tab.text)


args_parser = argparse.ArgumentParser()
args_parser.add_argument('folder', action='store', help='directory for saved tabs')
args = args_parser.parse_args()

folder = args.folder + '/'
if not os.path.exists(folder):
    os.makedirs(folder)

web_history = deque()
answer = input()
while not answer == 'exit':
    if answer == 'back':
        if len(web_history) > 1:
            web_history.pop()  # current page
            # This is code block because deque don't have peek() method
            back_page = web_history.pop()
            print_tab(back_page, folder)
            web_history.append(back_page)
    elif is_url_correct(answer, folder):
        save_tab(answer, folder)
        print_tab(answer, folder)
        web_history.append(answer)
    else:
        print('Error: Incorrect URL\n')
    answer = input()
