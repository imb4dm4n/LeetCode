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
- https://leetcode.com/problems/search-a-2d-matrix-ii/
- 240. Search a 2D Matrix II (Medium)
- 问题:  
在一个2D的行列都是递增的矩阵中, 找到特定的数字, 找不到返回 False
- 思路:
二分搜索从行开始，找不到则从列开始。
Beats 64.28%
- 思路2: O(m+n)
按行搜索, 在按列搜索
    '''
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # j = -1
        # for row in matrix:
        #     while j + len(row) and row[j] > target:
        #         j -= 1
        #     if row[j] == target:
        #         return True
        # return False

        def search_row():
            lo, hi  =   0, len(matrix[0]) 
            while lo < hi:
                mid     =   (hi+lo) // 2
                if matrix[0][mid] >= target: 
                    hi  =   mid # mid 在下一次循环不会被搜索
                elif matrix[0][mid] < target:
                    lo  =   mid     +   1
            return lo
        
        left  =   search_row()
        # left  = bisect_left(matrix[0], target)
        # 若找到了直接返回
        if left < len(matrix[0]) and matrix[0][left] == target:
            return True
        # 没找到， 则left那一列, 是最后一个大于 target 的索引, 因此需要 - 1
        if left == len(matrix[0]) or left > 0 :
            left    -=  1
        # search by column
        # print("left=",left)
        def search_column():
            nonlocal left
            lo, hi  =   0, len(matrix) 
            while lo < hi:
                mid     =   (hi + lo) // 2
                if matrix[mid][left] >= target: 
                    hi  =   mid
                elif matrix[mid][left] < target:
                    lo  =   mid     +   1
            # print("column=", lo)
            return lo
        while left >= 0:
            column  =   search_column()
            if column < 0 or column == len(matrix):
                return False
            if matrix[column][left]    ==  target:
                return True
            left -= 1
        return False
    
    '''
- https://leetcode.com/problems/find-peak-element/
- 162. Find Peak Element (Medium)
- 问题:  
peak 元素指的是它的值大于 左右相邻的 两个元素. 找出输入数组中任意一个 peak 元素: ie: nums = [1,2,1,3,5,6,4] -> Output: 5 . 因为 5 < 6 and 4 < 6; 返回 1 也可以, 因为 1 < 2.  时间复杂度必须是 logN.
超出边界的可以认定为比边界的小
- 思路:
二分搜索找到 mid 元素, 判断 mid + 1 and mid - 1 是否都小于 mid, 若 mid + 1
大于 mid, 则往右边找 lo = mid + 1, 若 mid - 1 也同时大于 mid 则同时往下找? ---- 
mid - 1 大于 mid 时往左边找 hi = mid - 1
Beats 95.15%
    '''
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) ==1:
            return 0
        
        n   =   len(nums)
        if nums[n-1] > nums[n-2]:
            return n - 1
        
        lo, hi  = 0, n - 1
        # 搜索空间 [0,n) 
        while lo <= hi:
            mid     =   lo + (hi-lo) // 2

            if nums[mid - 1] < nums[mid] and nums[mid + 1 ] < nums[mid]:
                return mid
            
            elif nums[mid - 1] > nums[mid]:
                # 左边的元素更大 调整 hi
                hi  =   mid - 1
            
            elif nums[mid + 1] > nums[mid]:
                # 右边的元素更大  调整 lo
                lo  =   mid + 1
        
        return -1
            

    '''
- https://leetcode.com/problems/binary-search/
- 704. Binary Search (Easy)
- 问题:  
实现二分搜索
- 思路:
上下界搜索 Beats 43.40%  和API Beats 86.30%
    '''
    def search(self, nums: List[int], target: int) -> int:
        left    =   bisect_left(nums, target)
        return left if left < len(nums) and  nums[left] == target else -1
        lo, hi = 0, len(nums) - 1
        while lo <= hi:
            mid     =   lo + (hi-lo) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo  =   mid + 1
            elif nums[mid] > target:
                hi  =   mid - 1
        
        return -1 


    '''
- https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
- 34. Find First and Last Position of Element in Sorted Array (Medium)
- 问题:  
输入一组升序排序的数组, 找到 target 的上界和下届索引. 不存在都返回-1
- 思路:
直接使用api即可
Beats 48.19%
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left    =   self.left_bound(nums,target)
        if left == -1:
            return [-1, -1]
        
        return [left, self.right_bound(nums, target)]

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
        lo,hi   =   0,len(nums) - 1
        while lo <= hi:
            mid     =   lo + (hi-lo) // 2
            if nums[mid] >= target:
                hi  =   mid - 1
            elif nums[mid] < target:
                lo  =   mid + 1
        return lo

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