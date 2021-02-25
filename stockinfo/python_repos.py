# -*- coding: utf-8 -*-
# @Time    : 2021-02-02 23:30
# @Author  : XU
# @File    : python_repos.py
# @Software: PyCharm
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS


url = 'https://api.github.com/search/repositories?q=language:python&sort=starts'
r = requests.get(url)
print(f"Status Code:{r.status_code}")
response_dict = r.json()
# print(response_dict.keys())

print(f"Total Count:{response_dict['total_count']}")
#
# print(f"Incomplete Results:{response_dict['incomplete_results']}")
#
# print(f"Item lens:{len(response_dict['items'])}")

# print(response_dict['items'][0].keys())
repo_dicts = response_dict['items']
names, stats = list(), list()
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stats.append(repo_dict['stargazers_count'])

# # for index in range(len(response_dict['items'])):
# for key in sorted(response_dict['items'][0].keys()):
#     # item_data = response_dict['items'][index]
#     # print(item_data.keys())
#     print(f"{key} : {response_dict['items'][0][key]}")
#     print('==============')

# 可视化
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('', stats)
chart.render_to_file('python_repos.svg')
