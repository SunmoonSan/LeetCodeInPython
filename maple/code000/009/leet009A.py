#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/9/30 23:37

"""
将整数转换为字符串, 对字符串进行判断比较简单, 但是整数转字符串的过程却是一个耗时的过程
整体看来, 这种算法思路简单, 但是效率不是很高
"""


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x == 0:  # 0是回文数
            return True
        elif x < 0:  # 负数不是回文数
            return False
        elif x > 0 and x % 10 == 0:  # 10, 100, 1000...不是回文数
            return False

        s = str(x)  # 整数转为字符串

        left = 0  # 左索引
        right = len(s) - 1  # 右索引
        while left < right:
            if s[left] != s[right]:  # 左右不相等
                return False

            left = left + 1  # 左索引右移
            right = right - 1  # 右索引左移

        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isPalindrome(0))
