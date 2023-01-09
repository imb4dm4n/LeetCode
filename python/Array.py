'''
数组操作的相关算法
'''

from typing import Optional, List
import heapq
import queue
import itertools

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
- https://leetcode.com/problems/range-sum-query-immutable/
- 303. Range Sum Query - Immutable (easy)
- 问题:  
输入一个不变的数组, 实现一个函数, 计算从 left到right索引的数字的和(包含left和right).
Input
["NumArray", "sumRange", "sumRange", "sumRange"]
[[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
Output
[null, 1, -1, -3]
- 思路:
前缀和思路: 用额外的空间 pre_sum, 在第i位, 存储从 0到i-1 的数字的和, 当需要计算 [i,j] 的和的时候,只需要用 pre_sum[j+1] - pre_sum[i] 即可.
可以理解为:
-----------[i]
---------------------[j+1]
***********----------[j+1 - i] => [i,j] 的和
Beats 76.4%
- 思路2:
用内置迭代器 Beats 97.85%
    '''
    class NumArray:
    
        def __init__(self, nums: List[int]):
            self.pre_sum    =   list(itertools.accumulate(nums))
            
            # self.pre_sum    =   [0] *   (nums.__sizeof__() + 1) # 需要额外一个空间
            # if nums.__len__() > 1:
            #     for i in range(1, nums.__len__() + 1):
            #         # 用前一个 前缀和 + 前一个数字 得到 当前 i 的 前缀和
            #         self.pre_sum[i] =   self.pre_sum[i-1]   + nums[i-1]
            # # 边界处理: 只有一个元素的时候
            # else:
            #     self.pre_sum[1] =   nums[0]
            

        def sumRange(self, left: int, right: int) -> int:
            if left == 0: return self.pre_sum[right]
            return self.pre_sum[right] - self.pre_sum[left-1]

            # return self.pre_sum[right+1] - self.pre_sum[left]

