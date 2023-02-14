'''
链表相关
'''

# Definition for singly-linked list.
from typing import Optional, List
from heapq import *
from queue import *
import types

class ListNode:
    pass

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # def __lt__(self, other):
    #     return self.val < other.val

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
    def print(node:ListNode, *args):
        '''
        输出node
        '''
        print("dump list:")
        l       =   ""
        while node:
            tmp = "->" if node.next else ""
            # print("{}".format(str(node.val) + tmp))
            l += str(node.val) + " -> "
            node        =   node.next
        for arg in args:
            print(arg)
        print(l[:-3])
        print("")

'''
# https://leetcode.com/problems/find-median-from-data-stream/
# 295. Find Median from Data Stream hard (hard)
问题: 实现一个类, 动态插入数据 以及 动态获取中位数.
思路:
把数字存储到 list 中, 然后需要求中位数的时候算一次 sorted ?
Runtime: 7465 ms, faster than 5.00% of Python3 online submissions for Find Median from Data Stream.
Memory Usage: 35.6 MB, less than 86.34% of Python3 online submissions for Find Median from Data Stream.
思路2: 平衡最大堆&最小堆
通过最大堆可以获取左半部分最大的值, 通过最小堆可以获取右半部分最小的值.
把输入的数据动态的插入到最大堆或最小堆中. 保持堆平衡.

先插入最大堆, 若最大堆数据比最小堆多, pop 一个最大堆的数据并转为负数到最小堆,
这样可以得到最大堆中的最小数字.
先插入最小堆, 若最小堆的数据比最大堆多, 那么把他 pop 出最小堆 写入最大堆.
计算中位数时, 若两个堆长度一样, 则把两个堆的顶部求和计算平均值即可;
若堆长度不一样, 取出
'''
class MedianFinder:
    def __init__(self):
        self.heaps = [], []

    def addNum(self, num):
        small, large = self.heaps
        heappush(small, -heappushpop(large, num))
        if len(large) < len(small):
            heappush(large, -heappop(small))

    def findMedian(self):
        small, large = self.heaps
        if len(large) > len(small):
            return float(large[0])
        return (large[0] - small[0]) / 2.0
    # def __init__(self):
    #     self.heaps       =   [],    []

    # def addNum(self, num: int) -> None:
    #     # small 是最小堆, large 是最大堆
    #     small, large    =   self.heaps
    #     heappush(large, num)
    #     if small.__len__() < large.__len__():
    #         # 最大堆移动一个到最小堆并转为负数
    #         heappush(small, -heappop(large))

    #     # self.data.append(num)

    # def findMedian(self) -> float:
    #     # small 是最小堆, large 是最大堆
    #     small, large    =   self.heaps
    #     if small.__len__() == large.__len__():
    #         print("small {} large {}".format(small, large))
    #         return (-small[0] + large[0]) / 2
    #     else:
    #         print("[+]small {} large {}".format(small, large))
    #         return -small[0]

        # self.data.sort()
        # if self.data.__len__() % 2 == 0:
        #     mid = int(self.data.__len__()/2)
        #     return  (self.data[mid-1] + self.data[mid]) / 2
        # else:
        #     return self.data[int(self.data.__len__() / 2)]

class Solution:
    '''
- replace with url
- replace with problem title
- 问题:  
replace with problem description
- 思路:
replace with your idea.
    '''
    '''
- https://leetcode.com/problems/merge-k-sorted-lists/
- 23. Merge k Sorted Lists Hard
- 问题:  
输入 k 条升序排序的链表, 合并他们为一个升序链表
- 思路:
一个链表头存储结果, 用最小堆存储链表头, 然后开始 heappop 弹出最小值, 并加入被弹出的那个节点的下一个节点, 直到堆为空.
Beats 88.77%
    '''
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        
        def lt(*args):
            pass
        ListNode.__lt__ =   types.MethodType(lt, ListNode)
        
        small_heap  =   []
        res     =   ListNode()
        ret     =   res
        
        for list_head in lists:
            if list_head:
                heappush(small_heap,
                    (list_head.val, list_head)
                    )
        

        while len(small_heap) > 0:
            top_val,top_node     =   heappop(small_heap)
            # print("cur top val {}".format(top_val))
            if top_node and top_node.next:
                heappush(small_heap, (top_node.next.val,top_node.next))
            res.next    =   top_node
            res         =   res.next
  
        # for i in range(len(small_heap)):
        #     print("heap ",heappop(small_heap))
                
        return ret.next

    
    '''
- https://leetcode.com/problems/linked-list-cycle-ii/
- 142. Linked List Cycle II Medium
- 问题:  
判断一个链表是否有环, 若有环, 则返回环的头节点
- 思路:
先判断是否有环, 然后返回环的一个节点, 计算环的长度.
让一个指针先移动环的长度, 然后另一个指针一起移动, 直到这两个指针相交,这时候就是指向环的入口节点.
Beats 72.41%
    '''
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def get_cycle_head(head: Optional[ListNode]) -> bool:
            '''
            获取环的头结点, 若不存在环, 则返回 None
            '''
            if not head or not head.next:
                return None
            
            slow,fast = head, head.next
            while fast and fast.next:
                if slow == fast:
                    return slow
                slow    =   slow.next
                fast    =   fast.next.next
            return None
        
        node    =   get_cycle_head(head)
        # 若没有环, 则直接返回 None
        if not node:
            return None
        
        # 计算环的长度
        cycle_len   =   1
        tmp     =   node
        while tmp and tmp.next != node:
            cycle_len   +=  1
            tmp     =   tmp.next
        
        # 先移动环的长度
        tmp     =   head
        while cycle_len > 0:
            tmp         =   tmp.next
            cycle_len   -=  1
        
        # 两个指针相遇时, 就是环的入口
        node    =   head
        while node != tmp:
            node    =   node.next
            tmp     =   tmp.next
        
        return node

    '''
- https://leetcode.com/problems/linked-list-cycle/description/
- 141. Linked List Cycle Easy
- 问题:  
检测链表是否有环
- 思路:
快慢双指针Beats 92.24%
    '''
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        
        slow,fast = head, head.next
        while fast and fast.next:
            if slow == fast:
                return True
            slow    =   slow.next
            fast    =   fast.next.next
        return False
        

    '''
- https://leetcode.com/problems/middle-of-the-linked-list/
- 876. Middle of the Linked List(easy)
- 问题:  
输入一个链表, 返回中间节点. 若是偶数个, 则返回后面一个
- 思路 
双指针移动.
Runtime: 37 ms, faster than 84.56% of Python3 online submissions for Middle of the Linked List.
Memory Usage: 13.8 MB, less than 55.96% of Python3 online submissions for Middle of the Linked List.
    '''
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow,fast    =   head, head
        while fast and fast.next:
            fast    =   fast.next.next
            slow    =   slow.next
        return slow
    '''
- https://leetcode.com/problems/remove-duplicates-from-sorted-array/
- 26. Remove Duplicates from Sorted Array(easy)
- 问题:  
输入一个升序排序的数组, 移除重复的数字, 得到唯一的数组,
不能分配额外空间, 只能修改原始数组, 返回唯一的数字个数 k
- 思路
栈的模拟. top 表示栈顶, 指向最新的非重复数字. 若不相同
则栈顶+1保存进来.
Runtime: 92 ms, faster than 92.50% of Python3 online submissions for Remove Duplicates from Sorted Array.
Memory Usage: 15.5 MB, less than 66.20% of Python3 online submissions for Remove Duplicates from Sorted Array.
    '''
    def removeDuplicates(self, nums: List[int]) -> int:
        if nums.__len__() == 0 or nums.__len__() == 1:
            return nums.__len__()
        last_unique =   nums[0]
        top         =   0

        for i in range(1, nums.__len__()):
            if nums[i] == last_unique:
                continue
            else:
                top     +=  1
                nums[top]    =   nums[i]
                last_unique     =   nums[i]
        
        # print("retuls {}".format(nums))
        return top+1
    '''
    # 2095. Delete the Middle Node of a Linked List
    # https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
    问题: 给定一个链表，删除它的中间节点, 返回修改后的链表头.
    middle从0开始计算. 比如n个节点, 那么中间节点是 n/2 取小于的整数
    思路:  之前有个思路是一个快慢指针, 快的移动两次, 慢的移动一次, 快的为None 时 慢的就是middle了.
    Runtime: 1913 ms, faster than 89.39% of Python3 online submissions for Delete the Middle Node of a Linked List.
    Memory Usage: 60.7 MB, less than 40.40% of Python3 online submissions for Delete the Middle Node of a Linked List
    '''
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy ,  fast  =   ListNode(), head
        dummy.next          =   head
        prev            =   dummy
        while fast and fast.next:
            fast    =   fast.next.next
            prev    =   prev.next
        
        # fast 为 None 时 , slow 指向中间节点, prev 是它的前一个
        prev.next   =   prev.next.next
        return dummy.next

    '''
    # 237. Delete Node in a Linked List
    # https://leetcode.com/problems/delete-node-in-a-linked-list/
    问题: 把输入的节点从链表删除. 约束: 非尾部节点.
    思路: 直接把下一个节点的值拷贝到当前节点即可
    Runtime: 96 ms, faster than 5.35% of Python3 online submissions for Delete Node in a Linked List.
    Memory Usage: 14.4 MB, less than 15.04% of Python3 online submissions for Delete Node in a Linked List.
    '''
    def deleteNode(self, node: Optional[ListNode]):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node:
            next_node   =   node.next
            node.val    =   next_node.val
            node.next   =   next_node.next
        
    '''
    # 92. Reverse Linked List II
    # https://leetcode.com/problems/reverse-linked-list-ii/
    问题: 输入一个链表 和 数字 left & right, 且 left<=right. 反转这区间的节点并返回链表.
    思路1: 定位需要反转的链表头和尾,
    思路2: 直接保存到数组, 进行反转. 需要额外空间
    思路3: 类似栈的操作, 不断的把需要反转的链表加入到"栈" 顶
    Runtime: 67 ms, faster than 17.27% of Python3 online submissions for Reverse Linked List II.
    Memory Usage: 14 MB, less than 52.02% of Python3 online submissions for Reverse Linked List II.
    '''
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or not head.next or\
            left == right:
            return head
        
        dummy, prev, cur    =   ListNode(), None, head
        prev        =   dummy
        prev.next   =   head

        # 移动到第一个反转点, prev 指向 "栈顶"
        for i in range(left-1):
            cur     =   cur.next
            prev    =   prev.next
        
        # 反转 m-n 次
        for i in range(right-left):
            # 把当前节点的下一个节点, 移动到 "栈顶"
            tmp     =   cur.next
            if not tmp:
                break
            cur.next    =   tmp.next
            top         =   prev.next   # 保存原始 "栈顶节点"
            prev.next   =   tmp
            tmp.next    =   top   # 新的 "栈顶节点"
        
        return dummy.next
                
    
    '''
    # 86. Partition List
    # https://leetcode.com/problems/partition-list/
    问题: 输入链表 和 值x, 在保持顺序的情况下, 根据 x 把链表分区, 使得 <x 的在前面, >x 在后面.
    思路: 生成两个链表, 一个链表保存小于x的节点, 另一个保存大于等于x的节点.
    变量声明: head_small(小于x的链表头), head_big(大于等于x的链表头), cur_small(小于x的链表cur指针),
    cur(原始链表工作指针)
    用 cur 遍历输入链表, 当 cur 小于 x 时, 把cur插入 small 链表(进行初始化), 大于x时, 把cur插入 big 链表(初始化),
    修复节点关系.
    边界情况:   所有节点都小于x 或 都大于等于x, 则不需要修改.
    Runtime: 67 ms, faster than 34.53% of Python3 online submissions for Partition List.
    Memory Usage: 13.9 MB, less than 77.20% of Python3 online submissions for Partition List.
    思路2: 同样是两个链表头, 额外构造指针.

    '''
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        # 思路2
        left_head       =   ListNode(None)  # head of the list with nodes values < x
        right_head      =   ListNode(None)  # head of the list with nodes values >= x
        left            =   left_head       # attach here nodes with values < x
        right           =   right_head      # attach here nodes with values >= x
        
        # traverse the list and attach current node to left or right nodes
        while head:
            if head.val < x:
                left.next   =   head
                left        =   left.next
            else:  # head.val >= x
                right.next  =   head
                right       =   right.next
            head    =   head.next
        
        right.next  =   None  # set tail of the right list to None
        left.next   =   right_head.next  # attach left list to the right
        
        return left_head.next 

        # 思路1
        if not head or not head.next:
            return      head
        
        head_small,head_big,cur_small,cur,prev      =   None,None,None,head,None
        while cur:
            if cur.val < x:
                if cur_small:
                    cur_small.next      =   cur
                if not head_small:
                    head_small          =   cur
                cur_small           =   cur
                cur             =   cur.next
                continue
            
            # 处理大于 等于的情况
            else:
                # 若已经有前一个大于等于的节点
                if prev:
                    prev.next   =   cur
                if not head_big:
                    head_big    =   cur
                prev        =   cur
                cur         =   cur.next
            
        # 所有都小于 或 都大于等于
        if not head_small or not head_big:
            return      head_small if not head_big else head_big
        # 修复关系
        cur_small.next  =   head_big
        prev.next       =   None
        return      head_small

    '''
    # 83. Remove Duplicates from Sorted List
    # https://leetcode.com/problems/remove-duplicates-from-sorted-list/
    问题: 输入一个链表, 删除重复的节点, 保持唯一. 类似做 set([]) 操作
    思路: 两个指针 prev, cur; prev 与 cur 不同时, 移动两个指针前进;
    相同时, 仅移动 cur 指针, 直到 cur 为空 或者 prev 与 cur 不同,修复 prev 的next
    然后移动两个指针.
    边界处理: 即使头结点重复, 也不用担心, 因为至少存在一个节点.
    所有节点值都一样, 则最后需要把头节点的next修改为 null;
    最后的节点是相同, 修改 prev 的 next 为 null;
    Runtime: 74 ms, faster than 50.50% of Python3 online submissions for Remove Duplicates from Sorted List.
    Memory Usage: 14 MB, less than 29.77% of Python3 online submissions for Remove Duplicates from Sorted List.
    '''
    def deleteDuplicates1(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # ListNode.print(head)
        prev,   cur =   head, head.next
        has_dup     =   False
        while cur:
            if prev.val ==  cur.val:
                cur         =   cur.next
                has_dup     =   True
                continue
            has_dup         =   False
            prev.next       =   cur
            prev            =   cur
            cur             =   cur.next
        # 边界处理
        if has_dup:
            prev.next       =   None
        return      head
        
    '''
    # 82. Remove Duplicates from Sorted List II
    # https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/
    问题: 输入一个排序的链表头, 移除存在重复的节点. ie: [1,2,3,3,3,4,4,5] => [1,2,5]
    思路1:  一个prev指针保存前一个节点, 一个cur指向当前节点, 若prev和当前节点相同,
    用递归吧, 每一层递归找到当前第一个非重复节点, 准备返回, 把递归下一层的节点设置为当前层的next
    思路2: 只有当前后两个节点不同, 且历史不发生重复, 才能把前一个节点加入到 唯一链表
    思路3:
    1,1,2 - 删除头节点&连续删除
    1,1,2,2 - 删除头节点&连续删除两组&返回空
    1,1,2,2,3 - 删除头节点&连续删除两组&返回非空
    1,2,2,3,3 - 删除非头节点 & 连续删除 & 最后为空
    1,2,2,3,3,4 - 删除非头结点 & 连续删除 & 最后非空
    Runtime: 80 ms, faster than 33.98% of Python3 online submissions for Remove Duplicates from Sorted List II.
    Memory Usage: 13.9 MB, less than 74.88% of Python3 online submissions for Remove Duplicates from Sorted List II.
    '''
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy       =   ListNode()
        cur_new     =   None
        prev,cur    =   head, head.next
        has_dup     =   False if head.val != cur.val else True
        while cur:
            # print("\nworking prev {} cur {}  dup {}".format(prev.val, cur.val, has_dup))
            if not has_dup and prev.val != cur.val:
                # 不曾重复过, 且当前值不等于prev, 说明 prev 唯一
                if not dummy.next:
                    dummy.next  =   prev
                    # print("Init head {}".format(prev.val))
                if cur_new:
                    cur_new.next=   prev
                cur_new =   prev
                prev    =   cur
                cur     =   cur.next
                continue
            # 和前一个值重复, 继续寻找, 直到找到不同 或者 cur 为 None
            if prev.val == cur.val:
                has_dup =   True
                cur     =   cur.next
                continue
            elif has_dup:
                prev    =   cur
                cur     =   cur.next
                has_dup =   False
                continue
        
        # print("\nworking prev {}  dup {} cur_new {}".format(prev.val,  has_dup, cur_new.val))
        if not has_dup and not dummy.next:
            dummy.next  =   prev
        if not has_dup and cur_new:
            cur_new.next    =   prev
        elif cur_new:
            cur_new.next    =   None    # 修复新链表最后一个节点
        # if tmp_cur:
        #     tmp_cur.next    =   None
        return dummy.next
        
        # print("working on {}".format(head.val))
        # prev,   cur =   None, head
        # has_dup     =   False
        # while cur:
        #     if cur.next:
        #         # 下一个节点和当前节点重复
        #         if cur.next.val == cur.val:
        #             has_dup =   True
        #             cur =   cur.next        # 没有考虑到, 若 cur 本身就存在重复的情况, 这样是不能作为唯一节点返回的
        #             continue
        #         elif has_dup:
        #             ret     =   cur.next
        #         else:
        #             ret     =   cur
        #         break
        #     elif has_dup:   # 和前一个节点相同, 且到达结尾了
        #         ret         =   None
        #     else:
        #         ret         =   cur
        #     break
        #     # if not prev :
        #     #     prev=   cur
        #     #     cur =   cur.next
        #     #     continue
        #     # if prev.val ==  cur.val:
        #     #     cur =   cur.next
        #     #     continue
        #     # ret     =   cur
        #     # break
        # if ret:
        #     print("ret = {}".format(ret.val))
        #     ret.next= self.deleteDuplicates(cur.next)
        # return      ret
        # pass
    
    '''
    # 21. Merge Two Sorted Lists
    # https://leetcode.com/problems/merge-two-sorted-lists/
    问题: 输入两个排序的链表头, 合并他们成为一个排序的链表, 返回合并的立案表头
    思路: 递归的合并两个链表的当前节点, 取出小的那个节点, 作为返回节点ret,
    递归得到下一层返回的节点, 设置为 ret 的 next. 直到两个链表为空.
    边界处理: 任意一个链表为空, 则直接返回非空的链表头
    Runtime: 42 ms, faster than 87.95% of Python3 online submissions for Merge Two Sorted Lists.
    Memory Usage: 14 MB, less than 32.77% of Python3 online submissions for Merge Two Sorted Lists.
    '''
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 迭代方式更快 Beats 84.31%
        ret     =   ListNode()
        res     =   ret
        p1 , p2 =   list1, list2
        while p1 and p2:
            if p1.val < p2.val:
                ret.next    =   p1
                p1          =   p1.next
            else:
                ret.next    =   p2
                p2          =   p2.next
            ret         =   ret.next
        if p1:
            ret.next    =   p1
        if p2:
            ret.next    =   p2
        return  res.next
        ret         =   None
        if not list1:
            return list2
        if not list2:
            return list1
        if list1.val < list2.val:
            ret     =   list1
            ret.next    =   self.mergeTwoLists(list1.next, list2)
        else:
            ret     =   list2
            ret.next    =   self.mergeTwoLists(list1, list2.next)
        return ret
    
    '''
    # https://leetcode.com/problems/remove-nth-node-from-end-of-list/
    # 19. Remove Nth Node From End of List
    问题: 输入一个链表, 删除倒数第 N 个节点, 返回链表头
    思路: 这不就是之前一直复习的. 若 N 小于链表长度 L, 则用两个指针 prev,cur.
    cur 先移动 N+1 次, 然后 prev 开始跟着移动. cur 为空的时候, prev 指向要删除的节点的前一个.
    边界处理: N=0(无意义), N=1(最后一个, 正常处理), N=L(删除头结点, 则需要修改head指针)
    异常处理: N > L (溢出)
    Runtime: 24 ms, faster than 99.75% of Python3 online submissions for Remove Nth Node From End of List.
    Memory Usage: 13.8 MB, less than 70.34% of Python3 online submissions for Remove Nth Node From End of List.
    '''
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev,cur        =   ListNode(), head
        prev.next       =   head
        
        for i in range(n):
            if cur:
                cur     =   cur.next
        
        while cur:
            cur         =   cur.next
            prev        =   prev.next
        
        # 删除头指针, 返回头指针的下一个
        if prev.next     ==  head:
            return      prev.next.next
        
        # 否则 prev.next 指向的是需要被删除的节点, 注意可能是最后一个节点
        prev.next   =   prev.next.next if prev.next else None
        return      head
        
    
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
            
# solution =  Solution()   
# -------------- 
# ret  = solution.deleteDuplicates(ListNode.list_to_ListNode([1,2,3,3,4,4,5]))
# ListNode.print(ret)
# ret  = solution.deleteDuplicates(ListNode.list_to_ListNode([1,1,2]))
# ListNode.print(ret)
# ret  = solution.deleteDuplicates(ListNode.list_to_ListNode([1,1,2,2]))
# ListNode.print(ret)
# ret  = solution.deleteDuplicates(ListNode.list_to_ListNode([1,1,2,2,3]))
# ListNode.print(ret)
# ret  = solution.deleteDuplicates(ListNode.list_to_ListNode([1,2,2,2,3]))
# ListNode.print(ret)

# -------------- 
# ret  = solution.removeNthFromEnd(ListNode.list_to_ListNode([1,2,3,4,5]), 2)
# ListNode.print(ret)
# ret  = solution.removeNthFromEnd(ListNode.list_to_ListNode([1,2]), 1)
# ListNode.print(ret)
# ret  = solution.removeNthFromEnd(ListNode.list_to_ListNode([1]), 1)
# ListNode.print(ret)

# -------------- 
# ret = solution.rotateRight(ListNode.list_to_ListNode([1,2]), 1)
# ListNode.print(ret)

# ret = solution.rotateRight(ListNode.list_to_ListNode([1,2,3,4,5]), 2)
# ListNode.print(ret)

# ret = solution.rotateRight(ListNode.list_to_ListNode([]), 2)
# ListNode.print(ret)