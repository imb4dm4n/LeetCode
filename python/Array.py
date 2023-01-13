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
- tag: 前缀和
- 思路:
replace with your idea.
    '''

    '''
- https://leetcode.com/problems/product-of-the-last-k-numbers/?show=1
- 1352. Product of the Last K Numbers(medium)
- 问题:  
实现一个类, 可以动态增加数字 并实现一个函数获取最后 k 个数的乘积, 可以确保至少有 k 个数.
productOfNumbers.add(3);        // [3]
productOfNumbers.add(0);        // [3,0]
productOfNumbers.add(2);        // [3,0,2]
productOfNumbers.add(5);        // [3,0,2,5]
productOfNumbers.add(4);        // [3,0,2,5,4]
productOfNumbers.getProduct(2); // return 20. The product of the last 2 numbers is 5 * 4 = 20
productOfNumbers.getProduct(3); // return 40. The product of the last 3 numbers is 2 * 5 * 4 = 40
productOfNumbers.getProduct(4); // return 0. The product of the last 4 numbers is 0 * 2 * 5 * 4 = 0
- tag: 前缀和
- 大神思路:
若出现一个0, 那么0之前的数的结果都是0, 因此直接更新数组为 [1]. 只记录 0 之后出现的数字结果.
假设输入 (a,b,c)
那么得到的 A = (a,a*b,a*b*c) 最大的乘积在栈顶
假设 k = 2, 那么结果便是
b * c = a*b*c / a = P[-1] // P[-2-1]
----------> 说白了就是前缀和, 第一部分 a 表示前一个区间的数字,
第二部分 b 表示k后半部分的数字的乘积, a * b = c(所有数字乘积), 因此 b = c / a

- 思路(超时, 太多没必要的计算):
前缀和的不变的数组, 这个是动态的数组. think in a reverse maner.
reserve a list for storing product of last k elements. 
以下算法会超时, 确实是缺乏一些洞见. 
1. 若在索引 i 加入一个 0 , 那么只要 k 个数大于 0 索引, 就一定为0, 因为乘数一定包含0. 因此记录 0 的最后一次索引 last_zero, 数据长度 n, 若 k >= n-last_zero, 那便可以直接返回 0
input_nums  =   []
surfix_product  =   []
---->
input_nums  =   [3]
surfix_product  =   [3]
---->
input_nums  =   [0,3]
surfix_product  =   [0,0]
---->
input_nums  =   [2,0,3]
surfix_product  =   [2,0,0]
---->
input_nums  =   [5,2,0,3]
surfix_product  =   [5,10,0,0]
---->
input_nums  =   [4,5,2,0,3]
surfix_product  =   [4,20,40,0,0] get(2) = surfix_product[2-1]
---->
input_nums  =   [8,4,5,2,0,3]
surfix_product  =   [8,32,160,320,0,0] get(2) = surfix_product[2-1]
    '''
    class ProductOfNumbers:
        def __init__(self):
            self.A = [1]

        def add(self, a):
            if a == 0:
                # 出现一个 0 则前面一切计算结果都没用了
                self.A = [1]
                print("add zero A = {}".format(self.A))
            else:
                # 和栈顶 前一个结果相乘
                self.A.append(self.A[-1] * a)
                print("add {} A = {}".format(a, self.A))

        def getProduct(self, k):
            # k 超过了最后一个 0 出现的位置, 因此结果一定为 0
            if k >= len(self.A): return 0
            # 用栈顶 除以 -k-1 的结果 得到 最后 k 个数字的结果
            # 栈顶是所有数字的乘积 因此是最大的, 作为 被除数
            # -k - 1 是最后 k 个数之前的所有数的乘积
            #
            return self.A[-1] // self.A[-k - 1]

        # def __init__(self):
        #     # self.input_nums =   []
        #     self.surfix_product =   []
        #     self.last_zero  =   -1
            

        # def add(self, num: int) -> None:
        #     # self.input_nums.insert(0, num)
        #     self.surfix_product.insert(0, num)
            
        #     if num == 0:
        #         self.last_zero  =   self.surfix_product.__len__() - 1
        #         print("lase_zero @ {}".format(self.last_zero))
        #     elif self.last_zero != -1:
        #         self.last_zero +=   1
        #         print("lase_zero @ {}".format(self.last_zero))
            
        #     for i in range(1,self.surfix_product.__len__()):
        #         # 若 乘积为0 , 则后续都没有必要计算了
        #         if not self.surfix_product[i]:
        #             break
        #         self.surfix_product[i]  *=   num
            
        #     print("add {} surfix {}".format(num, self.surfix_product))
            

        # def getProduct(self, k: int) -> int:
        #     if self.last_zero != -1 and k > self.last_zero:
        #         return 0
        #     return self.surfix_product[k-1]
            

    '''
- https://leetcode.com/problems/range-sum-query-2d-immutable/
- 304. Range Sum Query 2D - Immutable (medium)
- 问题:  
输入一个二维矩阵, 实现函数计算 由 (row1, col1) 为左上角坐标 (row2, col2).为右下角坐标构成的矩阵内, 所有的数字的和.
- tag: 前缀和
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
- tag: 前缀和
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

