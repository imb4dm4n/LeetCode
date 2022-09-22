'''
链表相关
'''

# Definition for singly-linked list.
from typing import Optional

class ListNode:
    pass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @staticmethod
    def list_to_ListNode(li:list):
        '''
        转输入的 数组为 ListNode 链表, 返回链表头
        '''
        ret_head        =   ListNode()
        prev            =   None
        for i in li:
            node        =   ListNode(i)
            if not ret_head.next:
                ret_head.next   =   node
            if prev:
                prev.next       =   node
            prev        =   node
        
        return  ret_head.next

    @staticmethod
    def print(node:ListNode):
        '''
        输出node
        '''
        l       =   ""
        while node:
            l += str(node.val) + " -> "
            node        =   node.next
        print(l[:-3])


class Solution:
    '''
    # https://leetcode.com/problems/rotate-list/
    # 61. Rotate List
    问题: 输入一个链表, 把它向右 循环移动 k 次
    思路1: 
    类似寻找倒数第 k 个节点, 先计算实际要移动的次数 x . 然后用3个指针: cur_head, prev, cur.
    cur 先移动 x - 1次, prev 指向cur前一个节点, 当 cur 移动 x-1 后,
    cur_head 开始移动, 直到 cur 指向 None. 此时 cur_head 指向需要断开的节点.
    [1,2] : 1 -> [2,1]
    [1,2,3,4,5] : 2 -> []
    负面处理: k<=0,不移动; 输入空链表 或 只有一个节点, 直接返回; 
    边界处理: k>链表长度, 则计算实际需要移动的次数.
    Runtime: 76 ms, faster than 22.37% of Python3 online submissions for Rotate List.
    Memory Usage: 14 MB, less than 31.62% of Python3 online submissions for Rotate List.
    
    思路2:
    用数组保存每个节点的地址, 直接根据索引来修改指针. 需要额外 O(N) 空间
    Runtime: 58 ms, faster than 59.84% of Python3 online submissions for Rotate List.
    Memory Usage: 14.1 MB, less than 31.62% of Python3 online submissions for Rotate List.
    '''
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        #  ------------------------- 思路2: -------------------------
        if not head or not head.next or k <= 0:
            return head
        li_addr             =   []
        list_len            =   0
        node                =   head
        while node:
            list_len        +=  1
            node            =   node.next
        k                   =   k % list_len
        node                =   head
        while node:
            li_addr.append(node)
            node            =   node.next
        
        new_head            =   li_addr[-k]
        break_point         =   li_addr[-(k+1)]
        li_addr[-1].next    =   head    # 修复最后一个节点
        break_point.next    =   None
        
        return      new_head
        
        #  ------------------------- 思路1: -------------------------
        if not head or not head.next or k <= 0:
            return head
        list_len            =   0
        cur,prev,cur_head   =   head, None, head # cur 指向 None时, prev 是最后一个节点指针, cur_head 是需要断链处的指针
        while cur:
            list_len        +=  1
            cur             =   cur.next
        k                   =   k % list_len    # 计算实际移动次数; 或者说 倒数第 k 个节点
        # 移动次数正好是链表长度的 整数倍, 相当于没有移动
        if k == 0:
            return head 
        # x                   =   0
        cur                 =   head
        for i in range(k+1):# 若 k 不加 1, 则会导致最后 cur_head 指向的是断链的后一个节点
        # while x < k+1:  # 若 k 不加 1, 则会导致最后 cur_head 指向的是断链的后一个节点
            # x           +=  1
            prev    =   cur         # 这里移动 prev 是为了解决 [1,2] : 1 这种输入情况, k+1=数组长
            cur         =   cur.next
        while cur:
            prev    =   cur         # cur 为None时, prev 指向最后一个节点
            cur         =   cur.next
            cur_head    =   cur_head.next
        
        ret_head        =   cur_head.next   # 返回新的头结点
        prev.next       =   head            # 修复最后一个节点的next为 头结点
        cur_head.next   =   None            # 修复断链处的 next 为 None
        return      ret_head

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
            
solution =  Solution()            
ret = solution.rotateRight(ListNode.list_to_ListNode([1,2]), 1)
ListNode.print(ret)

ret = solution.rotateRight(ListNode.list_to_ListNode([1,2,3,4,5]), 2)
ListNode.print(ret)

ret = solution.rotateRight(ListNode.list_to_ListNode([]), 2)
ListNode.print(ret)