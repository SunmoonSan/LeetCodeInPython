#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/1 20:58


class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = dict()  # 构造字典, nums元素为key, value任意
        for n in nums:
            if n in ans.keys():  # 字典有n这个key
                ans.pop(n)  # 从字典中删除n这个键
                continue  # 跳过本次循环
            ans[n] = 0  # 字典中不存在键n, 则加入字典, value为任意
        return list(ans.keys())[0]  # 将字典的keys转为列表,取列表第1个元素


if __name__ == '__main__':
    so = Solution()
    # nums = [2, 2, 1]
    nums = [4, 1, 2, 1, 2]
    print(so.singleNumber(nums))
