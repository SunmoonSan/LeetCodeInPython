#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018/9/29 10:14

"""
哈希表法, 从nums第一个元素开始, 逐步计算target-nums[i], 并判断其是否存在字典中, 若存在,则成功, 若不存在, 则加入到字典中.
字典是以nums中的元素为key, 对应索引为value
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        index_dict = dict()  # nums里元素为key, 对应索引为value
        n = len(nums)  # 列表nums的长度
        for i in range(n):
            other = target - nums[i]  # other是相对于target的差值
            if other in index_dict:  # 若other在字典中
                return [index_dict[other], i]  # 返回符合的2个值的索引
            index_dict[nums[i]] = i  # 若other不在字典中, 则将当前元素加到index_dict


if __name__ == '__main__':
    nums = [3, 2, 4]
    target = 6
    solution = Solution()
    p = solution.twoSum(nums, target)
    print(p)
