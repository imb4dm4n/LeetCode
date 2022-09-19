'''
链表相关
'''

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # https://leetcode.com/problems/swap-nodes-in-pairs/
    # 24. Swap Nodes in Pairs
    '''
    Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
    交换两个相邻的节点, 返回链表头. 不能修改节点的值. 注意: 节点个数可能为奇数个
    思路1: 
    递归交换两个节点, 返回交换后的 head 节点. 
    Runtime: 46 ms, faster than 63.93% of Python3 online submissions for Swap Nodes in Pairs.
    Memory Usage: 13.9 MB, less than 19.73% of Python3 online submissions for Swap Nodes in Pairs.
    '''
    def exchange(self, node:ListNode):
        '''
        交换 node 链表的两个节点, 返回交换后的节点头
        '''
        if not node or \
            not node.next:      # 节点的个数可能为奇数个
            return  node
        
        ret_head        =   node.next
        tmp             =   node.next.next  # 下一组需要交换的节点头
        node.next.next  =   node            # 当前节点的下一个节点, 修改指向为当前节点
        node.next       =   self.exchange(tmp)
        return          ret_head

    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret_head        =   ListNode()
        ret_head.next   =   self.exchange(head)
        return          ret_head.next

    # 优化代码:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Runtime: 54 ms, faster than 42.81% of Python3 online submissions for Swap Nodes in Pairs.
        Memory Usage: 13.9 MB, less than 19.73% of Python3 online submissions for Swap Nodes in Pairs.
        '''
        if not head or not head.next:
            return head
        
        next_node       =   head.next
        head.next       =   self.swapPairs(next_node.next)  # 修改当前节点的 next 为递归返回的
        next_node.next  =   head
        return          next_node       # 返回新的节点头


    # https://leetcode.com/problems/add-two-numbers/
    # 2. Add Two Numbers
    '''
    问题:
    You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.
    思路1:
    构建新的链表返回. head 保存返回的链表头, prev_node 表示前一个节点, cur_node 表示当前节点.
    用 prev 保存进位数值, 若最后没有节点了, 则需要分配一个节点作为最后的进位.
    '''
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], prev=0) -> Optional[ListNode]:
        '''
        Runtime: 164 ms, faster than 6.52% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 13.9 MB, less than 86.28% of Python3 online submissions for Add Two Numbers.
        '''
        head    =   None    # 保存返回节点
        prev    =   0       # 进位
        prev_node=  None    # 前一个节点需要修改 next
        while l1 or l2:
            sum_    =   (l1.val if l1 else 0 ) + (l2.val if l2 else 0) + prev 
            node    =   ListNode(sum_%10)
            prev    =   sum_ // 10
            # 前一个节点需要修改 next
            if prev_node:
                prev_node.next  =   node
            prev_node       =   node
            if not head:
                head    =   node
            if l1:
                l1  =   l1.next
            if l2:
                l2  =   l2.next
        
        # 注意最后的进位
        if prev:
            node    =   ListNode(prev)
            prev_node.next  =   node
        return  head
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode], prev=0) -> Optional[ListNode]:
        '''
        :parma      prev    前一步进位的结果
        思路2:
        类似合并两个链表的思路: 若其中一个链表为空, 直接返回另一个. 若都不为空, 创建一个节点 tmp, 
        pop两个链表, 计算两个节点的和保存到tmp, 取出进位给下一个递归函数计算下去.
        Runtime: 149 ms, faster than 13.94% of Python3 online submissions for Add Two Numbers.
        Memory Usage: 13.9 MB, less than 86.28% of Python3 online submissions for Add Two Numbers.
        '''
        # 递归结束
        if not l1 and not l2:
            # ------------ 非常隐晦的点, 当两个都为空的时候, 但是存在 prev , 需要创建一个
            if not prev:
                return None
            else:
                return ListNode(prev)
        
        # 其中一个为空, 计算进位
        if not l1:
            sum_    =   l2.val  + prev
            if sum_ < 10:
                l2.val  =   sum_
                return l2
            else:
                l2.val  =   sum_ % 10
                l2.next =   self.addTwoNumbers(l1, l2.next, sum_//10)
                return l2
        if not l2:
            sum_    =   l1.val  + prev
            if sum_ < 10:
                l1.val  =   sum_
                return l1
            else:
                l1.val  =   sum_ % 10
                l1.next =   self.addTwoNumbers(l1.next, l2, sum_//10)
            return l1
        # 两个都不为空
        tmp     =   ListNode()
        sum_    =   l1.val + l2.val + prev      # 记得需要加上进位
        tmp.val =   sum_ % 10
        tmp.next=   self.addTwoNumbers(l1.next, l2.next, sum_//10)
        return tmp
        
        # 若其中一个为空
        # if len(l1) == 0 or len(l2) == 0:
        #     return  [l1, l2][len(l1)==0]
        
        # head    =   ListNode()
        # prev_node=  None
        # prev    =   0
        # cur_1:ListNode   =   l1[0]
        # cur_2:ListNode   =   l2[0]
        # while cur_1 or cur_2:
        #     sum =   0
        #     cur     =   ListNode()
        #     if not head.next:
        #         head.next   =   cur
        #     if cur_1:
        #         sum +=  cur_1.val
        #     if cur_2:
        #         sum +=  cur_2.val
            
        #     prev    =   sum // 10
        #     sum     =   sum % 10
        #     cur.val =   sum
            