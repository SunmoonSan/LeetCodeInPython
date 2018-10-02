#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/1 21:11


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0  # 0和任何数异或运算,不改变任意数值
        for n in nums:
            res = res ^ n  # list中所有元素进行异或, 数字相同异或值为0

        return res


if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3, 4, 5]
    so.singleNumber(nums)
    print(1 ^ 1)
    print(1 ^ 0)
    print(0 ^ 0)
    print(0 ^ 1 ^ 0 ^ 1 ^ 3)  # 3
