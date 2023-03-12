'''
二分搜索
'''
from typing import Optional, List
import heapq
import queue
from collections import *
from bisect import *
import math

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
- https://leetcode.com/problems/koko-eating-bananas/
- 875. Koko Eating Bananas (Medium)
- 问题:  
有 piles 组香蕉, 每一组有i个香蕉, 守卫h小时会回来. KOKO 每小时可以吃k个,每小时吃完k不吃别的组, 问最少的k可以在守卫回来前吃完香蕉.
Input: piles = [3,6,7,11], h = 8
Output: 4
- 思路:
和昨天公交车有点像? 每小时吃k个, 那么第 j 个小时可以吃的总数量就是 j * k.
当 j = 8 的时候必须吃完所有香蕉 sum(piles). 
应该是一样的: 假设最慢的时候每次吃11个,那么8小时吃 8 * 11 = 88 > sum(piles),
这时候找到 mid 值计算. 其实就是找第一个大于等于 sum(piles)的  h * k
Beats 71.88%
    '''
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lo, hi = 0, max(piles)       # 可以吃的香蕉 总数区间

        def calc_total_eat(k):
            '''
            给定每小时吃的香蕉数k, 返回 h 小时能不能吃完 total_banana
            '''
            if k == 0:
                return False
            c = 0
            for banana in piles:
                c += math.ceil(banana/k) 
            return c <= h

        while lo < hi:
            # 每小时吃x个香蕉, 吃h小时的总数
            mid     =   (lo+hi)//2
            # 不能直接乘法, 因为提到了吃完一堆不吃另一堆, 导致吃的时候不均匀. 即给定每小时 mid 个香蕉, 需要优化其能够吃的个数
            if calc_total_eat(mid):
                hi  =   mid # 注意使用的是 lo < hi搜索区间是 [lo,hi) 因此不用 -1
            else:
                lo  =   mid + 1
                
        if not calc_total_eat(lo):
            return lo + 1
        
        return lo 
    
    '''
- https://leetcode.com/problems/minimum-time-to-complete-trips/
- 2187. Minimum Time to Complete Trips (Medium)
- 问题:  
输入一组数字表示第i个公交车完成一轮行程的耗时,每个公交车可以连续来回行程并互不影响.
输入totalTrips表示所有公交车可以完成的行程数, 问最少时间完成totalTrips是多少? 
Input: time = [1,2,3], totalTrips = 5
Output: 3
Explanation:
- At time t = 1, the number of trips completed by each bus are [1,0,0]. 
  The total number of trips completed is 1 + 0 + 0 = 1. // 时间 1 只有一辆车完成
- At time t = 2, the number of trips completed by each bus are [2,1,0]. 
  The total number of trips completed is 2 + 1 + 0 = 3. // 时间 2 有两辆车完成 且第一列跑了两次
- At time t = 3, the number of trips completed by each bus are [3,1,1]. 
  The total number of trips completed is 3 + 1 + 1 = 5.
So the minimum time needed for all buses to complete at least 5 trips is 3.
- 思路:
找出最快的那辆车, 计算它完成所有行程的耗时, 得到时间遍历的次数.
遍历时间h, 每个h对应可以计算出完成的车辆个数, 加入到 时间-完成车辆次数组, 
然后二分查找这个数组 第一个大于等于 totalTrips 的索引+1即可.
超时了....
提示是如何计算给定时间所有车辆完成的次数
- 大神思路: Beats 86.75%
先计算最快的车完成耗时, 作为搜索上界.
二分查找这个耗时, 计算对应耗时完成的
- 找到不变的是什么, 变化的是什么? 时间在每一刻是确定的, 每一刻对应完成的数量是不同的, 不同时间有不同的完成数量. 找到一个时间它的完成数量大于目标即可. 随着时间在增大, 完成数量也是增大, 因此都是递增的序列. 推导出基于时间的二分搜索. 
    '''
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        least_time  =   min(time) * totalTrips
        lo, hi = 0, least_time + 1
        def is_complete_total_trip(when):
            '''
            判断给定时刻, 所有车辆完成的次数是否大于等于 totalTrips
            '''
            return sum(when//t for t in time) >= totalTrips

        while lo < hi:
            mid = (lo+hi) // 2
            if is_complete_total_trip(mid):
                hi  = mid
            else:
                lo  = mid + 1
            
        return lo 
    
        time_complete_bus   =   []  # 每一个存储第 i 小时完成 trip 的车辆个数
        for h in range(1, least_time+1):
            now_complete    =   0
            for i in time:
                now_complete    +=  h // i
            time_complete_bus.append(now_complete)
        
        return bisect_left(time_complete_bus, totalTrips) + 1
    
    '''
- https://leetcode.com/problems/kth-missing-positive-number/
- 1539. Kth Missing Positive Number (Easy)
- 问题:  
输入一组升序排序的数字, 返回丢失的第k个整数. 
Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. The 5th missing positive integer is 9.
- 思路1:
简单的线性扫描? Beats 23.21%
- 思路2:
二分搜索, mid 必须大于左边1 小于右边1, 否则说明其中一边存在元素丢失.
如果两边都有丢失, 则递归两边的搜索, 否则只搜索一边.
从1-n升序排序, 每个数字减去对应的索引, 可以得到这个数之前丢失的个数.
Beats 79.2%
    '''
    def findKthPositive2(self, arr: List[int], k: int) -> int:
        lo, hi = 0, len(arr)
        while lo < hi:
            mid     =   (lo+hi) //  2
            num     =   arr[mid] - mid -1 # 丢失的数字个数
            # print("mid={} n={} num={}".format(mid, arr[mid],num))
            if num < k:
                lo  =   mid + 1
            else:
                hi  =   mid
        
        if lo> -1 and lo < len(arr):
            print("lo={} lo_n={} ".format(lo, arr[lo]))
        return k + lo


    def findKthPositive(self, arr: List[int], k: int) -> int:
        # lo, hi = 0, len(arr)
        # while lo < hi:
        #     mid     =   (lo+hi) //  2
        #     if mid - 1 > -1 and mid + 1 < len(arr):
        #         if arr[mid-1]

        for i in range(1, arr[-1]):
            if i in arr:
                continue
            else:
                k   -=  1
                if k == 0 :
                    return i
        return k + arr[-1]
    
    '''
- https://leetcode.com/problems/search-in-rotated-sorted-array/
- 33. Search in Rotated Sorted Array (Medium)
- 问题:  
输入一个有序数组, 它可能被旋转了，也可能没被旋转, 找到 target
- 大神思路:
核心思想: 二分查找的数组一定是一个升序的数组, 把部分非升序的屏蔽掉, 得到升序数组.
根据 mid 和 t 是否在同一边, 做不同处理: 
    1.若 mid 和 t 在同一边, 那么其实就是普通的二分搜索即可.
    2.若 mid 和 t 不再同一边, 那么根据 mid 和 t 的关系, "调整" mid 的值,使得数组是有序的. 
        比如 mid < t(5) : 那么让 mid = +INFINITY 这样能使得数组变成[4,5,6,7,+INF(mid),+INF] 数组还是有序的; 
        或者 t(3) < mid : 那么让 mid = -INF 使得数组变成 [-INF,-INF(mid),1,2,3,4]

ie: 4,5,6,7, 1,2,3,4. 若 mid 和 t 在同一边, 那么他们一定在 [ 4,5,6,7], 或者 [1,2,3,4] 区间内.


二分搜索, 并根据 mid 判断往那个方向移动.
根据 nums[0] 和 nums[mid] 的关系, 判断 mid 落在的区间是哪一部分.
nums[0] > nums[mid] 说明落在了旋转的右侧;
nums[0] < nums[mid] 说明落在了旋转的左侧;
判断 target 和 nums[mid] 的关系, 跳转 lo 或 hi
Beats 85.98%
    '''
    def searchx(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi) // 2
            if target < nums[0] < nums[mid]:
                # 能够保证 target 在右侧 , 并且搜索区间往右边靠拢
                lo = mid + 1
            elif nums[mid] < nums[0] <= target:
                # 能够保证 target 在左侧, 并且搜索区间朝左边缩小
                hi = mid
            elif nums[mid] < target:
                lo = mid + 1
            elif target < nums[mid]:
                hi = mid
            else:
                return mid
        
        return -1
        
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