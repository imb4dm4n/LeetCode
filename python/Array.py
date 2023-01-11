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
- https://leetcode.com/problems/range-sum-query-2d-immutable/
- 304. Range Sum Query 2D - Immutable (medium)
- 问题:  
输入一个二维矩阵, 实现函数计算 由 (row1, col1) 为左上角坐标 (row2, col2).为右下角坐标构成的矩阵内, 所有的数字的和.
- 思路:
二维前缀和: 用大的矩阵减去小的矩阵, 补上丢失的矩阵, 即可得到结果.
(row2,col2) - (row2,col1) - (row1,col2) + (row1,col1)
xxxxxx  xxxxxx
xxxxxx  xxyyyx 
xxxxxx  xxyyyx
xxxxxx  xxyyyx
===>
aaaaxx   bbxxxx   ccccxx   ddxxxx
aaaaxx - bbxxxx - ccccxx + ddxxxx
aaaaxx   bbxxxx   xxxxxx   xxxxxx
aaaaxx   bbxxxx   xxxxxx   xxxxxx
用一个更大的二维矩阵保存每个坐标到(0,0)构成的矩阵的数字的和.
area(x,y) = area(x-1,y) + area(x,y-1) - area(x-1,y-1)
Beats 56.2%
    '''
    class NumMatrix:

        def __init__(self, matrix: List[List[int]]):
            # 初始化二维矩阵: 不能直接 * 10, 否则相当于是对同一个矩阵的 10 次引用
            self.pre_sum_matrix =   [ [0] * (len(matrix[0]) +1) for _ in range((len(matrix) +1)) ]
            for row in range(1, len(matrix)+1):
                for col in range(1, len(matrix[0])+1):
                    # matrix[row-1][col-1] 因为矩阵被扩大了
                    # - self.pre_sum_matrix[row - 1][col - 1] 是因为 加上两个矩阵时, 重复加了 area(row-1, col-1) 这个矩阵, 因此要减去一次
                    self.pre_sum_matrix[row][col]   =   matrix[row-1][col-1] \
                        + self.pre_sum_matrix[row][col - 1] \
                        + self.pre_sum_matrix[row-1][col]  \
                        - self.pre_sum_matrix[row - 1][col - 1]

                    print("r {} c {} d {} sum {}".format(row, col, matrix[row-1][col-1], self.pre_sum_matrix[row][col]  ))
            
        def _get_region(self, row, col):
            if row < 0 or col < 0:
                return 0
            return self.pre_sum_matrix[row][col]

        def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
            # (row2,col2) - (row2,col1) - (row1,col2) + (row1,col1)
            # 由于前缀和被扩大了1层, 因此获取时需要把坐标+1. 如 获取 matrix(1,1) 到 matrix(0,0) 的前缀和, 实际需要获取 pre_sum_matrix(2,2)
            return self._get_region(row2+1,col2+1) -\
                    self._get_region(row1,col2+1) - \
                        self._get_region(row2+1,col1) + \
                            self._get_region(row1,col1)

        def print_pre_sum_matrix(self):
            for i in range(self.pre_sum_matrix.__len__()):
                print(self.pre_sum_matrix[i])

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

