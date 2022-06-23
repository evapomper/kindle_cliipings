import re
import pandas as pd

def read_clippings(c_file):
    with open(c_file, 'r', encoding="utf8") as f:
        return f.read().splitlines()


def divide_clippings(raw):
    return [raw[i:i + 5] for i in range(0, len(raw), 5)]


def create_dict_clippings(clip):
    my_clippings = {'author': [], 'title': [], 'adding_time': [], 'quote': []}
    for i in range(len(clip)):
        ta = re.split(r'[()]', clip[i][1])
        my_clippings['author'].append(ta[1])
        my_clippings['title'].append(ta[0])
        add = clip[i][2].split("|")
        my_clippings['adding_time'].append(add[1])
        my_clippings['quote'].append(clip[i][4])
    return my_clippings

my_clippings_raw = read_clippings('My Clippings.txt')
my_clippings_list = divide_clippings(my_clippings_raw)
my_clipping_list_edit = my_clippings_list.pop(-1)
my_clippings_dict = create_dict_clippings(my_clippings_list)

df = pd.DataFrame(my_clippings_dict)
df.to_excel('./clippings.xlsx')

