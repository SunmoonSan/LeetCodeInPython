#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @desc : Created by San on 2018/10/5 09:49


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 链表为空, 直接返回空
        if head is None:
            return head

        # 为链表构造一个虚拟头结点
        dummy_head = ListNode(-1)
        dummy_head.next = head

        p = head
        # 遍历链表, 两个节点相同,则跳过后面的节点,不同则指针p后移1位
        while p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p = p.next

        return dummy_head.next
