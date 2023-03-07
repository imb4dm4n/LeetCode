import sys
from typing import List
from typing import Optional
from unittest   import *
import unittest
import collections
from itertools import *
from BinarySearch import Solution as SB
from bisect import *

bs  =   SB()


def maxNumOfMarkedIndices(nums: List[int]) -> int:
    c   =   0
    times   =   len(nums) // 1
    nums.sort()
    print(nums)
    for i in range(times):
        if len(nums) ==0 :
            break
        max_num =   nums[-1]
        # 找到第一个小于等于 max_num 一半的
        half_max_num    =   max_num//2
        i   =   bisect_left(nums, half_max_num)
        if i > 0 and nums[i]!= half_max_num:
            i   -=  1
        print("i=",i," = ", nums[i])
        if nums[i] * 2 > max_num:
            i   =   -1
        print("[!!!]{} 一半是 {} 移除位置是 {} num={}".format(max_num, half_max_num, i, nums[i]))
        if i == -1:
            nums.pop()
        else:
            nums.pop(i)
            nums.pop()
            print("nums update ", nums)
            c   +=  2
        # if i != -1: 
        #     nums.pop(i)
        #     nums.pop()
        #     print("nums update ", nums)
        #     c   +=  2
    print(nums)
    return c

r=maxNumOfMarkedIndices([42,83,48,10,24,55,9,100,10,17,17,99,51,32,16,98,99,31,28,68,71,14,64,29,15,40])
print("r={} == 26?".format(r))
exit(0)

r=maxNumOfMarkedIndices([1,78,27,48,14,86,79,68,77,20,57,21,18,67,5,51,70,85,47,56,22,79,41,8,39,81,59,74,14,45,49,15,10,28,16,77,22,65,8,36,79,94,44,80,72,8,96,78,39,92,69,55,9,44,26,76,40,77,16,69,40,64,12,48,66,7,59,10])
print("r={} == 64?".format(r))
# exit(0)
r=maxNumOfMarkedIndices( [3,5,2,4])
print("r={}".format(r))
r=maxNumOfMarkedIndices([9,2,5,4])
print("r={}".format(r))
r=maxNumOfMarkedIndices([7,6,8])
print("r={}".format(r))
exit(0)

'''
- https://leetcode.com/contest/weekly-contest-334/problems/find-the-divisibility-array-of-a-string/
- 6368. Find the Divisibility Array of a String
- 问题:  
输入一个数字字符串, 返回由这个字符串子序列组成的数字能否被m整除.
Input: word = "998244353", m = 3
Output: [1,1,0,0,0,1,1,0,0]
Explanation: There are only 4 prefixes that are divisible by 3: "9", "99", "998244", and "9982443".
- 思路:
除法的本质是什么? n 个 基数 的和 得到 target,
一个数 x 如果可以整除另一个数 y, 那么 x%y = 0, 那么 x * 10 % y == 0.
也就是乘以10肯定还是可以整除的, 那么只需要判断新加入的那个数字能不能整除即可.
prev_divisable 表示前一个构成的数能否整除，初始为 True,
若当前数字可以整除则结果为1, 若不能则为0 , 且
prev_num 表示前一个数, 和当前的数组合成新数...
如果 被除数是一个 大一些的数字, 那么计算会很耗时的 ...
这是一个除法优化问题 不会- -
或者说是一个因式分解问题? x= abcde = q x w x e x r;
y = opqr = o x p x q x r
'''
def divisibilityArray(word: str, m: int) -> List[int]:
    ans     =   [0] * len(word)
    prev_num=   1
    prev_divisable  =   True
    for i,c in enumerate(word):
        if prev_divisable:
            if int(c)%m == 0:
                # print("[+] {} {} is divable".format(prev_num, c))
                ans[i]  =   1
            else:
                prev_divisable  =   False
                prev_num    =   int(c)
                # print("update prev num {}".format(prev_num))
        else:
            prev_num    *=  10
            # print("[adding] {} {} num={}".format(i,c, prev_num))
            prev_num    +=  int(c)
            if prev_num % m == 0:
                ans[i]  =   1
                # print("[!]{} is divable".format(prev_num))
                prev_divisable  =   True
            # else:
            #     print("not divable {}".format(prev_num))
    
    return ans

print("r={}".format(r)) 
r = divisibilityArray("529282143571", 4)
print("r={}".format(r)) 
if r != [0,1,0,1,1,0,0,0,0,0,0,0]:
    print("Failed")
else:
    print("OK")

# exit(0)

r = divisibilityArray(word = "998244353", m = 3)
print("r={}".format(r))
'''
9,
99,
998,    0
9982,   0
99824,  0
998244, 1
'''
if r != [1,1,0,0,0,1,1,0,0]:
    print("Failed")
else:
    print("OK")

r = divisibilityArray(word = "1010", m = 10)
print("r={}".format(r)) 
if r != [0,1,0,1]:
    print("Failed")
else:
    print("OK")


exit(0)

'''
- https://leetcode.com/contest/weekly-contest-334/problems/left-and-right-sum-differences/
- 6369. Left and Right Sum Differences
- 问题:  
Given a 0-indexed integer array nums, find a 0-indexed integer array answer where:

answer.length == nums.length.
answer[i] = |leftSum[i] - rightSum[i]|.
Where:

leftSum[i] is the sum of elements to the left of the index i in the array nums. If there is no such element, leftSum[i] = 0.
rightSum[i] is the sum of elements to the right of the index i in the array nums. If there is no such element, rightSum[i] = 0.
- 思路:
前缀和 和 后缀和
'''
def leftRigthDifference(nums: List[int]) -> List[int]:
    ans     =   [0] * len(nums)

    prefix_sum  =   list(accumulate(nums))
    prefix_sum.insert(0,0)
    nums.reverse()
    surfix_sum  =   list(accumulate(nums))
    surfix_sum.insert(0,0)
    surfix_sum.reverse()
    # print(prefix_sum,"\n",surfix_sum)
    for i in range(0,len(nums)):
        # print(prefix_sum[i], surfix_sum[i+1])
        ans[i]  =   abs(prefix_sum[i] - surfix_sum[i+1])
    return ans
    # pre,sur =   0,0

    # for i in range(len(nums)):
    #     ans[i] +=   pre
    #     pre     +=  nums[i]
    #     ans[-i-1]+= sur
    #     sur     +=  nums[-1]
    # print(ans)
    # return ans

r=leftRigthDifference( nums = [10,4,8,3])
print("r={}".format(r))
r=leftRigthDifference( nums = [1])
print("r={}".format(r))
exit(0)

'''
任意一个数都可以表示为
2^a + 2^b + 2^c + ...
39 = 0x27
0010 0111 + 1 = 40 
0010 1000 - 2^3  = 32
0010 0000 - 2^5  = 0
=0
--------
54 = 0x36
0011 0110 + 2
0011 1000 + 8 
0100 0000 - 2^6 
Input: n = 54
Output: 3
Explanation: We can do the following operations:
- Add 21 = 2 to n, so now n = 56.
- Add 23 = 8 to n, so now n = 64.
- Subtract 26 = 64 from n, so now n = 0.
So the minimum number of operations is 3.

-----------
把从右往左第一个1左边的0变成1
或者说让 1 慢慢的变成 0 即可.
... 可以减去一个数
'''
def minOperations(n: int) -> int:
    def power_of_2(num:int):
        '''
        若一个数是 2 的 n 次方, 返回True
        '''
        if (num-1) & num == 0:
            return True
        return False

    def make_1_to_0(num:int):
        '''
        把输入的 num 的1变成0
        18-> 0001 0010
        0001 0110 -》 加法
        0010 0100 -> 用减法
        应该是这样, 输入的数字 num 如果连续的1比较多, 那么用加法,
        如果输入的 num 低位 只有 1个1, 那么用减法
        '''
        # print("make {} to zero ".format(num))
        if num&1:
            return 1
        # 找到从右往左第一个1的位置, 返回 2^pos
        pos = 0
        while not num&1:
            num     //=   2
            pos += 1
        # print("pos = {} num = {} {} ".format(pos, num, (num//2)&1))
        if not (num//2)&1:
            # 后面还有1 那么用加法
            while  num&1:
                num     //=   2
                pos += 1
            # print("用加法 ")
            return 2 ** pos
        else:
            # 用减法
            # print("用减法 ")
            return - (2 ** pos)
    count = 1

    while not power_of_2(n):
        x   =  make_1_to_0(n)
        # print("x={} n={} n+x = {}".format(x,n,n+x))
        n +=    x
        count +=    1
    
    return count
    square  =   int(n**0.5)
    low,high    =   square **2, (square+1) **2
    distance    =   min((n-low), (high-n))
    print("low {} high {} distance {}".format(low, high, distance))


# r=minOperations(39)
# print("r={}".format(r))

r=minOperations(54)
print("r={}".format(r))