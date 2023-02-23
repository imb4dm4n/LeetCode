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
    def left_bound(self, nums:list, target):
        '''
        在 nums 中搜索target, 返回最左边那个; 找不到返回 -1
        '''
        if not nums:
            return -1
        left, right = 0, len(nums) - 1

        while left <= right:
            mid     =   left + (right - left) // 2
            if nums[mid] == target:
                right   =   mid - 1 
            elif nums[mid] < target:
                left    =   mid + 1
            elif nums[mid] > target:
                right   =   mid - 1
        
        # 若 target 是最大的数字, 那么 left = mid + 1 可能溢出
        if left == len(nums):
            return -1
        
        # 这时 left 一定可以访问
        return left if nums[left] == target else -1
        

    def right_bound(self, nums:list, target):
        '''
        在 nums 中搜索target, 返回最右边那个;  找不到返回 -1
        '''
        if not nums:
            return -1

        left, right = 0, len(nums) - 1
        while left <= right:
            mid     =   left + (right - left) // 2
            if nums[mid] == target:
                left    =   mid + 1     #   导致 break 时 mid 可能不指向 target, 因此 循环外部要访问的是 left - 1
            elif nums[mid] < target:
                left    =   mid + 1
            elif nums[mid] > target:
                right   =   mid - 1
        
        # 若 target 是一个很小的数, 那么 left 可能为0 寻找的目标是 mid - 1 会溢出
        if left - 1 < 0:
            return -1

        return left - 1 if nums[left - 1] == target else -1 

    '''
- https://leetcode.com/problems/ipo/
- 502. IPO (Hard)
- 问题:  
leetcode 要上市, 有初始 w的资金 和 最多k项独立完成的项目， 每个项目有初始投资 capital[i] 和收益 profit[i], 问最大的资金是多少?
- 思路:
获取小于等于 w 资金的所有项目列表, 同时进行 profit 排序找出最大收益项目, w - capital[i] + profit[i] 更新w的同时, 移除完成的项目, k - 1; 直到 k = 0 退出循环
    '''
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        map_invest  =   dict(zip(capital, profits))
        
        while k > 0 :
            pass

    '''
- https://leetcode.com/problems/single-element-in-a-sorted-array/
- 540. Single Element in a Sorted Array (Medium)
- 问题:  
输入一个有序的数组, 除了一个元素外, 其他元素都出现两次, 找出那个元素。
- tag: search,sorted array, 
- 思路:
在不存在单一元素的前提下, 访问 奇数索引的元素, 那么它的前一个元素和它相同，
访问偶数索引的元素，那么它的后一个元素和它相同；
通过二分搜索找到mid元素，判断mid的索引找到应该和它相同的元素；
- 思路2: O(N)时间
亦或每个字符, 结果就是那个数字了.... 机智啊... 虽然慢了一些
    '''
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        # 因为有单一元素所以 right= 偶数 mid 也一定是偶数? 
        # 偶数则下一个元素必定是相同的 否则 下一个就是单一的元素
        while left < right:
            mid     =   left + (right - left)//2
            # 奇数转偶数
            if mid & 1 :
                mid -= 1
            # 说明左侧的元素多了，向左侧搜索
            if nums[mid] != nums[mid+1]:
                right = mid
            # 否则在右侧, 由于 mid 和 mid + 1 已经是相同的 所以 left 需要 mid + 2
            else:
                left = mid + 2 
            
        return nums[left]
            
            
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