'''
数组操作的相关算法
'''

from operator import mul
from typing import Optional, List
import heapq
import queue
import itertools
from collections import *
from itertools import *
from math import *

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
- https://leetcode.com/problems/maximum-sum-circular-subarray/
- 918. Maximum Sum Circular Subarray (medium)
- 问题:  
输入一个可以循环使用的数组, 返回 非空子数组的和 的最大值. 
循环使用意思是 数组结尾可以连接到数组头, the next element of nums[i] is nums((i+1)%n) and previous element is nums[(i-1+n)%n]. 非空子数组元素不能重复使用.
- tag: 
- 思路:
这也是前缀和吧, 不过是可以循环出去
    '''

    '''
- https://leetcode.com/problems/count-of-range-sum/
- 327. Count of Range Sum(hard)
- 问题:  
输入一组数字和两个整数 lower 和 upper, 返回所有 和能够在 lower & upper 区间的 子数组个数.
Input: nums = [-2,5,-1], lower = -2, upper = 2
Output: 3
Explanation: The three ranges are: [0,0], [2,2], and [0,2] and their respective sums are: -2, -1, 2.
- tag: 前缀和
- 思路:
难道是枚举范围列表, 然后每个查询一次前缀和?  肯定得超时, 这个枚举的数量太大了.

    '''
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        pre_sum     =   [0] * (len(nums) + 1)
        count       =   0
        for i in range(1, len(nums)+1):
            pre_sum[i]  =   pre_sum[i-1]    +   nums[i-1]
        
        # print("pre sum {}".format(pre_sum))

        def get_range_sum(begin, end):
            return pre_sum[end+1] - pre_sum[begin]
        
        # for i,j in combinations(range(len(nums)),2):
        for i,j in combinations_with_replacement(range(len(nums)),2):
            range_sum   =   get_range_sum(i, j)
            if lower <= range_sum and range_sum <= upper:
                count   +=  1
            # print(i, j, get_range_sum(i, j))
        
        return count

    '''
- https://leetcode.com/problems/product-of-array-except-self/
- 238. Product of Array Except Self (medium)
- 问题:  
输入一个数组 nums, 返回一个数组, ans[i] 表示除了 nums[i] 外所有数字的乘积.
可否用 O(1) 的空间解决问题.
- tag: 前缀和
- 思路:
朴素的想法, 除开0,求所有数字的乘积, 然后再一个一个除过去.
1. 包含 1 个 0, 那么只有0所在的索引有结果, 其他都是0
2. 包含 2 个 0, 那么结果都是0
3. 不包含 0, 用总的乘积除以每一个
Beats 99.22%
- 大神思路
前缀和与后缀和的思路. 用一个前缀乘积pre[] 和 后缀乘积sur[] 保存 [0, i-1]的乘积 和
[i+1, -1] 的乘积. 这样计算 ans[i] = pre[i-1] * sur[i+1]. 比如
[1,2,3,   4,  5,6,7] => ans[3] = pre[2] * sur[4] = (1*2*3)  * (5*6*7).
优化空间:
直接把前缀乘积存储到输出ans, 然后第二次遍历后缀乘积时, 再对 输出数组ans进行更新.
    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 进一步优化成一次遍历
        n,pre,sur   =   len(nums), 1, 1
        ans     =   [1] * len(nums)

        for i in range(n):
            ans[i] *=   pre
            pre    *=   nums[i]

            ans[-1-i]   *=  sur
            sur     *=  nums[-1-i]
        
        return ans

        # 大神优化空间
        ans     =   [1] * len(nums)
        sur_product =   1
        n       =   len(nums)
        for i in range(1, n):
            ans[i]  =   ans[i-1] * nums[i-1]
        
        print(ans)
        for i in range(n-1, -1, -1):
            print("i={} num={}".format(i, nums[i]))
            ans[i]      *=  sur_product
            sur_product *=  nums[i]
        
        print(ans)
        return ans


        # 大神思路
        pre     =   list(accumulate(nums, mul))
        sur     =   list(accumulate(nums[::-1], mul))[::-1]     # 内部的反转是为了从尾部开始计算, 第二次反转是为了可以直接使用 sur[i+1] 进行索引
        n       =   len(nums)
        
        ans     =   []
        for i in range(len(nums)):
            ret = (pre[i-1] if i > 0 else 1) * (sur[i+1] if i+1 < n else 1)
            ans.append(  ret )
            print("i={} ret = {} x= {} y = {}".format(i, ret, (pre[i-1] if i > 0 else 1) , (sur[i+1] if i+1 < n else 1)))
            
        print("num = {} ".format(nums))
        print("pre = {} {}".format(pre, list(accumulate(nums, mul))))
        print("sur = {} {}".format(sur, list(accumulate(nums[::-1], mul))))
        print("ans = {}".format(ans))
        
        return ans

        # 思路1
        count_num   =   Counter(nums)
        # 2 个 0 直接返回
        if count_num.get(0) and count_num.get(0) > 1:
            return [0]  * len(nums)

        # 1 个0 或 没有 0
        product     =   1
        zero_pos    =   -1
        ret     =   [0] * len(nums)

        for i, n in enumerate(nums):
            if n :
                product    *=   n
            else:
                zero_pos    =   i
        
        # 存在 1 个 0
        if zero_pos != -1:
            ret[zero_pos]   =   product
            return ret
        
        # 没有 0
        for i,n in enumerate(nums):
            ret[i] = product // n
        
        return ret

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
- https://leetcode.com/problems/matrix-block-sum/
- 1314. Matrix Block Sum(medium)
- 问题:  
输入一个 m x n 的矩阵 mat 和整数 k , 返回矩阵 answer 其中 answer[i][j] 是 所有在 mat[r][c] 矩阵中的元素的和.:
i-k <= r <= i+k
j-k <= c <= j+k
(r,c)是矩阵中有效的位置.
- tag: 前缀和
- 思路:
说白了, 就是以每个坐标 (i,j)向外扩张 k 行 和 k列, 得到的矩阵, 里面所有元素的和, 写到 answer[i][j].
应该是可以复用 304 题的代码. 画一张图就知道了. 其实就是复用 304 的代码, 计算出向外扩张后的矩阵的左上角坐标和右下角坐标, 然后求矩阵内所有元素的和即可.
Beats 66.3%
    '''
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        matrix  =   self.NumMatrix(mat)
        matrix.print_pre_sum_matrix()
        ans     =   [[0] * mat[0].__len__() for _ in range(mat.__len__())]

        for i in range(mat.__len__()):
            for j in range(mat[0].__len__()):
                left_up     =   [i-k, j-k]
                if left_up[0] < 0:
                    left_up[0]  =   0
                if left_up[1] < 0:
                    left_up[1]  =   0
                
                right_down  =   [i+k, j+k]
                if right_down[0] >= len(mat):
                    right_down[0]   =   len(mat) -1
                if right_down[1] >= len(mat[0]):
                    right_down[1]   =   len(mat[0]) - 1
                ans[i][j]   =   matrix.sumRegion(left_up[0], left_up[1], right_down[0], right_down[1])

        # print("ans {}".format(ans))
        return ans

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

