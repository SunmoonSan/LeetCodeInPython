#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/1 00:21
"""
将每个字符串按字符顺序排序后作为字典的key, 字符串本身作为字典的value
"""
import collections


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        ans = collections.defaultdict(list)  # list类型为value的字典
        for s in strs:
            key = tuple(sorted(s))  # dict的key必须为不可变量, 转为tuple
            ans[key].append(s)

        return list(ans.values())  # ans.values()格式化成列表


if __name__ == '__main__':
    so = Solution()
    t = ["eat", "tea", "tan", "ate", "nat", "bat"]
    d = so.groupAnagrams(t)
    print(type(d), d)
