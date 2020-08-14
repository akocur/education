import argparse
import os


nytimes_com = '''
This New Liquid Is Magnetic, and Mesmerizing

Scientists have created “soft” magnets that can flow 
and change shape, and that could be a boon to medicine 
and robotics. (Source: New York Times)


Most Wikipedia Profiles Are of Men. This Scientist Is Changing That.

Jessica Wade has added nearly 700 Wikipedia biographies for
 important female and minority scientists in less than two 
 years.

'''

bloomberg_com = '''
The Space Race: From Apollo 11 to Elon Musk

It's 50 years since the world was gripped by historic images
 of Apollo 11, and Neil Armstrong -- the first man to walk 
 on the moon. It was the height of the Cold War, and the charts
 were filled with David Bowie's Space Oddity, and Creedence's 
 Bad Moon Rising. The world is a very different place than 
 it was 5 decades ago. But how has the space race changed since
 the summer of '69? (Source: Bloomberg)


Twitter CEO Jack Dorsey Gives Talk at Apple Headquarters

Twitter and Square Chief Executive Officer Jack Dorsey 
 addressed Apple Inc. employees at the iPhone maker’s headquarters
 Tuesday, a signal of the strong ties between the Silicon Valley giants.
'''


def get_short_url(url):
    dot_position = url.rfind('.')
    return url if dot_position == -1 else url[:dot_position]


def is_url_correct(url, folder):
    return is_url_exist(url) or os.path.exists(folder + url)


def is_url_exist(url):
    return url in ('bloomberg.com', 'nytimes.com')


def print_tab(url, folder):
    with open(folder + get_short_url(url)) as tab:
        print(tab.read())


def save_tab(url, folder):
    if not is_url_exist(url):
        return
    tab = globals()[url.replace('.', '_')]
    with open(folder + get_short_url(url), 'w') as file:
        file.write(tab)


args_parser = argparse.ArgumentParser()
args_parser.add_argument('folder', action='store', help='directory for saved tabs')
args = args_parser.parse_args()

folder = args.folder + '/'
if not os.path.exists(folder):
    os.makedirs(folder)

answer = input()
while not answer == 'exit':
    if is_url_correct(answer, folder):
        save_tab(answer, folder)
        print_tab(answer, folder)
    else:
        print('Error: Incorrect URL\n')
    answer = input()
