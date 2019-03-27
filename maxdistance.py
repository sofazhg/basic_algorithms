#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 17:05
# @Author  : Zhang Shaohau
# @Site    : sofazhg@outlook.com
# @File    : maxdistance.py
# @Software: PyCharm

import random

num_list = []
n = 50
for i in range(n):
    num_list.append(random.uniform(1, 100))

print(num_list)
max = max(num_list)
min = min(num_list)
sum_distance = max - min
aver_distance = sum_distance / (n - 1)

list = []
for i in range(n):
    list.append([])

for num in num_list:
    index = int((num - min) / aver_distance)
    if len(list[index]) == 0:
        list[index].append(num)
        list[index].append(num)
    else:
        if num < list[index][0]:
            list[index][0] = num
        elif num > list[index][1]:
            list[index][1] = num

list2 = []
for l in list:
    if len(l) != 0:
        list2.append(l)

maxdistance = 0
for j in range(len(list2) - 2):
    temp = list2[j + 1][0] - list2[j][1]
    if temp > maxdistance:
        maxdistance = temp

print(maxdistance)
