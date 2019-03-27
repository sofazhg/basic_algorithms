#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/3/21 22:16
# @Author  : 
# @Site    : 
# @File    : maxdiff.py
# @Software: PyCharmUPGIVEUP

def maxDiffSubArrays(nums):
    # write your code here
    if (len(nums) == 2): return abs(nums[0] - nums[1])
    # dpleftmax、dprightmax数组记录每个位置结尾的子数组最大和
    # dpleftmin、dprightmin数组记录每个位置结尾的子数组最小和
    # dpleftmax从左到右遍历
    dpleftmax = [0 for i in range(len(nums))]
    maxp = -99999
    sum = 0
    for i in range(0, len(nums)):
        if (sum < 0):
            sum = nums[i]
        else:
            sum += nums[i]
        maxp = max(maxp, sum)
        dpleftmax[i] = maxp

    # dprightmax从右到左遍历
    dprightmax = [0 for i in range(len(nums))]
    maxp = -99999
    sum = 0
    for i in range(len(nums) - 1, -1, -1):
        if (sum < 0):
            sum = nums[i]
        else:
            sum += nums[i]
        maxp = max(maxp, sum)
        dprightmax[i] = maxp

    # dpleftmin从左到右遍历
    dpleftmin = [0 for i in range(len(nums))]
    minp = 99999
    sum = 0
    for i in range(0, len(nums)):
        if (sum > 0):
            sum = nums[i]
        else:
            sum += nums[i]
        minp = min(minp, sum)
        dpleftmin[i] = minp

    # dprightmin从右到左遍历
    dprightmin = [0 for i in range(len(nums))]
    minp = 99999
    sum = 0
    for i in range(len(nums) - 1, -1, -1):
        if (sum > 0):
            sum = nums[i]
        else:
            sum += nums[i]
        minp = min(minp, sum)
        dprightmin[i] = minp

    # dpleftmax里存的是每个位置左边子数组最大和，dprightmax里存的是每个位置右边子数组最大和
    # 所以最后统计一遍两者之和最大值
    maxp = -99999999
    for i in range(1, len(dpleftmax)):
        sum1 = abs(dpleftmax[i - 1] - dprightmin[i])
        sum2 = abs(dpleftmin[i - 1] - dprightmax[i])
        sum = max(sum1, sum2)
        if (sum > maxp):
            maxp = sum

    return maxp


print(maxDiffSubArrays([1, 2, -3, 1]))
