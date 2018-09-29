#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc  : Created by San on 2018/9/29 09:11
"""
暴力双层循环方法在数据量比较大的情况下, 时而能通过, 时而不能通过. 不是一个优秀的算法.
"""


class Solution:
	def twoSum(self, nums, target):
		"""
		:type nums: List[int]
		:type target: int
		:rtype: List[int]
		"""
		for i in range(len(nums)):  # i是第一层索引
			for j in range(i + 1, len(nums)):  # j是第二层索引
				if nums[i] + nums[j] == target:  # 索引i位置的数和索引j位置的数和为target
					return [i, j]  # 返回结果为list类型


if __name__ == '__main__':
	nums = [2, 7, 11, 15]
	target = 9
	solution = Solution()
	p = solution.twoSum(nums, target)
	print(p)
