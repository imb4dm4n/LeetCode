'''
二分搜索
'''
from typing import Optional, List
import heapq
import queue
from collections import *
from bisect import *


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
- https://leetcode.com/problems/search-insert-position/
- 35. Search Insert Position (Easy)
- 问题:  
输入一个有序集合和一个数字n，返回插入n的索引使得数组还是排序的。
- 思路:
二分搜索第一个大于等于n的数字
找得到就返回数字的索引， 找不到，则break时，left=right+1 可能会溢出, 做一次检测
- 二分搜索
    找得到: 直接返回了
    找不到: break 时, nums[left] / nums[right] / target 的关系
Beats 96.78%
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums, target)
        
        left,right = 0, len(nums) - 1
        
        # 有可能无法在区间 [0, right] 找到大于 target的数
        if nums[-1] < target :
            return right + 1
        
        # 第一个数字就大于target
        elif nums[0] >= target and right == 0:
            # print("direct return")
            return 0

        while left <= right:
            mid     =   left + (right-left)//2
            # print("left {} right {} mid {}".format(left,right,mid))
            if nums[mid] > target:
                # 若大于则 mid - 1 这样break时可能是 nums[mid] < target
                right  = mid - 1
            elif nums[mid] < target:
                left  = mid + 1 
            elif nums[mid] == target:
                # print("return mid")
                return mid

        if nums[left] < target and (left+1) <= (len(nums) -1) and nums[left+1] > target :
            return left + 1
        # 默认break情况是 nums[left] > target
        return left