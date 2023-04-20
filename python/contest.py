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

from collections import *
'''
-   
- 问题:     
- 思路:  
'''
'''
-   https://leetcode.com/contest/weekly-contest-340/problems/sum-of-distances/
- 问题:     6360. Sum of Distances
输入一个数组, 返回一个数组, 每个 res[i] 表示任何和 输入数字 Num[i] 相等的数字 num[j] 他们的距离的总和. res[i] = |i-j| + |i-j1| + ...
Input: nums = [1,3,1,1,2]
Output: [5,0,3,4,0]
Explanation: 
When i = 0, nums[0] == nums[2] and nums[0] == nums[3]. Therefore, arr[0] = |0 - 2| + |0 - 3| = 5. 
When i = 1, arr[1] = 0 because there is no other index with value 3.
When i = 2, nums[2] == nums[0] and nums[2] == nums[3]. Therefore, arr[2] = |2 - 0| + |2 - 3| = 3. 
When i = 3, nums[3] == nums[0] and nums[3] == nums[2]. Therefore, arr[3] = |3 - 0| + |3 - 2| = 4. 
When i = 4, arr[4] = 0 because there is no other index with value 2. 
- 思路:  
统计数字出现的次数, 遍历数字, 若为0个直接写0, 若大于1个, 则
'''

class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res     =   [0] * n 
        cm = Counter(nums)
        np  =   defaultdict(list)

        for i,m in enumerate(nums):
            np[m].append(i)

        for i,num in enumerate(nums):
            if cm[num] == 0:
                continue
            poss    =   np[num] # 得到数字的索引列表
            poss.remove(i)
            for a in poss:
                res[i] += abs(i-a)
            poss.append(i)
        return res
so = Solution()
r=so.distance([[1,3],[2,3]])
print("r= ", r)

'''
-   https://leetcode.com/contest/weekly-contest-340/problems/prime-in-diagonal
- 问题:    6361. Prime In Diagonal 
输入一个2d矩阵, 返回对角线上数字中最大的 质数
- 思路:  
'''
class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        max_prime   =   0
        n   =   len(nums)
        def is_prime(val):
            half    =   int(val**0.5 + 1)
            for i in range(2, half):
                if val % i == 0:
                    return False
            return True
        # print(len(nums), len(nums[0]))
        # print("483 ?", is_prime(483))
        for i in range(n):
            if is_prime(nums[i][i]):
                max_prime=max(max_prime, nums[i][i])
            if is_prime(nums[i][n-i-1]):
                max_prime=max(max_prime, nums[i][n-i-1])
        return max_prime

so = Solution()
r=so.diagonalPrime([[1,3],[2,3]])
print("r= ", r)
r=so.diagonalPrime([[788,645,309,559],
                    [624,160,435,724],
                    [770,483,95,695],
                    [510,779,984,238]])
print("r= ", r)
r=so.diagonalPrime( [[1,2,3],[5,17,7],[9,11,10]])
print("r= 17 ？", r)
r=so.diagonalPrime([[395,777,912,431,42,266,989,524,498,415,941,803,850,311,992,489,367,598,914,930,224,517,143,289,144,774,98,634],[819,257,932,546,723,830,617,924,151,318,102,748,76,921,871,701,339,484,574,104,363,445,324,626,656,935,210,990],[566,489,454,887,534,267,64,825,941,562,938,15,96,737,861,409,728,845,804,685,641,2,627,506,848,889,342,250],[748,334,721,892,65,196,940,582,228,245,823,991,146,823,557,459,94,83,328,897,521,956,502,112,309,565,299,724],[128,561,341,835,945,554,209,987,819,618,561,602,295,456,94,611,818,395,325,590,248,298,189,194,842,192,34,628],[673,267,488,71,92,696,776,134,898,154,946,40,863,83,920,717,946,850,554,700,401,858,723,538,283,535,832,242],[870,221,917,696,604,846,973,430,594,282,462,505,677,657,718,939,813,366,85,333,628,119,499,602,646,344,866,195],[249,17,750,278,120,723,226,381,814,175,341,437,836,64,104,802,150,876,715,225,47,837,588,650,932,959,548,617],[697,76,28,128,651,194,621,851,590,123,401,94,380,854,119,38,621,23,200,985,994,190,736,127,491,216,745,820],[63,960,696,24,558,436,636,104,856,267,72,227,74,663,309,359,447,185,63,516,479,41,611,104,717,401,205,267],[368,927,750,482,859,924,941,584,174,715,689,209,990,786,60,808,693,163,866,166,351,543,257,121,612,944,453,682],[180,14,483,698,420,922,583,896,521,940,319,665,366,398,858,674,257,158,575,708,13,469,760,81,344,757,47,558],[288,139,246,781,977,494,361,625,295,690,368,605,970,914,649,875,636,136,733,318,398,767,425,849,667,83,2,609],[197,716,343,164,246,229,653,459,388,728,897,690,582,896,425,33,412,893,719,582,429,791,679,727,48,170,457,66],[266,719,162,458,541,907,499,930,575,619,774,1,906,40,507,334,320,858,479,52,829,843,897,998,832,426,193,562],[987,649,86,858,743,134,16,412,973,695,428,324,4,219,15,735,773,3,843,692,542,627,101,196,122,623,665,204],[895,310,287,706,187,103,488,875,945,407,643,84,23,282,936,464,820,812,119,883,263,137,670,534,837,667,661,356],[118,893,159,286,872,20,44,42,211,698,266,572,323,970,376,961,582,932,870,44,867,768,985,719,623,672,507,730],[660,925,470,656,446,382,893,551,183,213,385,602,299,10,142,155,278,342,346,809,377,736,96,347,799,636,37,43],[277,168,154,598,297,370,405,562,133,301,118,490,749,246,957,50,316,184,878,536,747,73,310,413,856,337,307,425],[112,102,575,931,493,486,346,862,818,1000,832,352,128,491,119,717,510,437,39,310,344,753,704,916,160,942,171,642],[579,385,826,998,655,90,68,828,87,203,768,227,63,395,9,101,404,570,532,297,460,943,501,808,599,732,696,223],[434,86,378,226,268,600,796,171,442,197,368,118,66,842,885,874,719,29,925,539,463,771,694,207,122,510,408,263],[213,657,44,971,817,222,639,150,108,203,470,388,371,560,847,155,108,611,500,152,578,416,654,697,434,899,534,508],[696,940,910,331,854,511,511,651,687,896,207,556,625,954,225,10,349,723,986,765,921,326,838,330,37,538,152,896],[264,618,803,160,863,389,597,302,736,724,827,482,68,820,87,529,890,938,41,68,231,134,42,308,16,778,865,460],[339,883,165,820,153,890,672,472,992,381,518,392,923,543,515,35,588,93,695,814,825,531,777,615,79,765,437,928],[773,212,297,549,923,613,428,846,996,494,866,811,996,398,623,601,240,872,886,818,21,673,907,1,759,187,310,520]])
print("r= 833 ?", r)
exit(0)

'''
- https://leetcode.com/contest/weekly-contest-339/problems/mice-and-cheese/
- 问题:    6364. Mice and Cheese
 
- 思路:  
'''

'''
-   https://leetcode.com/contest/weekly-contest-339/problems/convert-an-array-into-a-2d-array-with-conditions/ 
- 问题:    6363. Convert an Array Into a 2D Array With Conditions
输入一个数组, 构造一个 2d 数组, 每一行都是不同的数字, 并且行数最少. 
- 思路:  
用计数器统计所有数字个数, 当任意数字的个数大于0时, 加入到当前数组,
并把所有的都 - 1
'''
class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        cn  =   Counter(nums)
        res     =   []
        while sum(cn.values()) > 0:
            tmp     =   []
            for n,c in cn.items():
                if c > 0:
                    tmp.append(n)
                    cn[n] = c - 1
            res.append(tmp)
        return res



so = Solution()
r=so.findMatrix(nums = [1,3,4,1,2,3,1])
print("r=", r)
r=so.findMatrix(nums = [1,2,3,4])
print("r=", r)

exit(0)

'''
-   https://leetcode.com/contest/weekly-contest-339/problems/find-the-longest-balanced-substring-of-a-binary-string/ 
- 问题:    6362. Find the Longest Balanced Substring of a Binary String
输入一个二进制数字符串，一个子串是平衡的：0在1前面，且他们的个数是一样。 找出最长的平衡子串的长度。
Input: s = "01000111"
Output: 6
Explanation: The longest balanced substring is "000111", which has length 6.
- 思路:  
边界情况： 都是0或者1， 直接返回0
平衡问题, 感觉是用栈, 用0栈和1栈.
初始化 need_calc = False
遍历当前的字符, 遇到0加入0栈, 遇到1加入1栈,
若0和1数量都大于0,则开始计算是否平衡 ?

'''
class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        if '0' not in s or \
            '1' not in s:
            return 0
        
        # print("\n\ns= ", s)
        stack_0, stack_1    =[],[]
        longest     =   0
        for i,c in enumerate(s):
            if len(stack_1) > 0 and c == '0':
                # 存在1 但是遇到0了, 需要清除
                stack_0, stack_1    =[],[]
                # print("存在1 但是遇到0了, 需要清除 ",i, stack_0, stack_1)

            if c == '0':
                stack_0.append(c)
            else:
                stack_1.append(c)
            
            if len(stack_0) > 0 and \
                len(stack_1) > 0:
                longest     =   max(longest, 2 * min(len(stack_0), len(stack_1)))
                # print("longse = {} s0 {} s1 {}".format(longest, len(stack_0), len(stack_1)))
                # stack_0, stack_1    =[],[]
            
        return longest

so = Solution()
r=so.findTheLongestBalancedSubstring(s = "01000111")
print("r=", r)

r=so.findTheLongestBalancedSubstring(s = "01010100011001")
print("r=", r)

r=so.findTheLongestBalancedSubstring(s = "00111")
print("r=", r)

r=so.findTheLongestBalancedSubstring(s = "111")
print("r=", r)

exit(0)

'''
-  https://leetcode.com/contest/weekly-contest-337/problems/the-number-of-beautiful-subsets/
-  6352. The Number of Beautiful Subsets
- 问题:    
输入一组数字找到所有子数组, 任意两个数字的差的绝对值不等于k, 统计子数组个数

- 思路: 
动态规划, 添加一个新的数字前提是, 他的 +-k的目标不在已经存在的map中
'''
import copy 
class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count =   0
        def bp_add_num(datas:list, want_cur:bool, prev_map:dict):
            nonlocal total_count,k
            if not datas:
                return
            
            # tmp=copy.deepcopy(prev_map)
            print("datas: {} prev_map {} want_cur {}".format(datas, prev_map, want_cur))
            has_cur =   False
            if want_cur:
                n   =   datas[0]
                if not prev_map[n+k] and not prev_map[n-k]:
                    print("n={} datas: {} , prevmap= {} c={}".format(n, datas,prev_map, total_count))
                    total_count +=  1
                    prev_map[n] +=  1
                    has_cur =   True
            #     bp_add_num(datas[1:], True, prev_map)
            #     bp_add_num(datas[1:], False, prev_map)
            # else:
            bp_add_num(datas[1:], True, prev_map)
            bp_add_num(datas[1:], False, prev_map)
            # if has_cur:
            #     prev_map[n] -=  1
        
        pm  =   defaultdict(int)
        bp_add_num(nums, True, pm)
        pm  =   defaultdict(int)
        bp_add_num(nums, False, pm)
        return total_count


so= Solution()
r=so.beautifulSubsets(nums = [2,4,6], k = 2)
print("r= {} == 4 ?".format(r))
r=so.beautifulSubsets([4,2,5,9,10,3] , 1)
print("r= {} == 23 ?".format(r))
exit(0)
r=so.beautifulSubsets(nums = [2,4,6,8], k = 2)
print("r= {} == 4 ?".format(r))
r=so.beautifulSubsets( nums = [1], k = 1)
print("r= ", r)
exit(0)

'''
-  https://leetcode.com/contest/weekly-contest-337/problems/check-knight-tour-configuration/
-  6322. Check Knight Tour Configuration
- 问题:    
输入一个数字, 返回二进制上在 奇数索引和偶数索引有多少个1
Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001. 
It contains 1 on the 0th and 4th indices. 
There are 2 even and 0 odd indices.

- 思路: 
'''

'''
-  https://leetcode.com/contest/weekly-contest-337/problems/number-of-even-and-odd-bits
-  6319. Number of Even and Odd Bits
- 问题:    
输入一个数字, 返回二进制上在 奇数索引和偶数索引有多少个1
Input: n = 17
Output: [2,0]
Explanation: The binary representation of 17 is 10001. 
It contains 1 on the 0th and 4th indices. 
There are 2 even and 0 odd indices.

- 思路: 
'''
class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        index   =   0
        c_odd,c_eve =   0,0
        while n:
            if n & 1:
                if not index&1:
                    c_eve   +=  1
                else:
                    c_odd   +=  1
            n//=2
            index   +=  1
        return [c_eve, c_odd]

so= Solution()
r=so.evenOddBit(17)
print("r= ", r)
r=so.evenOddBit(2)
print("r= ", r)

'''
- https://leetcode.com/contest/weekly-contest-336/problems/rearrange-array-to-maximize-prefix-score/
- 6316. Rearrange Array to Maximize Prefix Score
- 问题:   
输入一组数字, 对他们进行重排序, 使得他们的前缀和数组 prefix_sums 能够尽可能多的有正数,
一个正数算1分, 问最多可以得到多少分? 
Input: nums = [2,-1,0,1,-3,3,-3]
Output: 6
Explanation: We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
prefix = [2,5,6,5,2,2,-1], so the score is 6.
It can be shown that 6 is the maximum score we can obtain.
- 思路: 
'''


'''
- https://leetcode.com/contest/weekly-contest-336/problems/rearrange-array-to-maximize-prefix-score/
- 6316. Rearrange Array to Maximize Prefix Score
- 问题:   
输入一组数字, 对他们进行重排序, 使得他们的前缀和数组 prefix_sums 能够尽可能多的有正数,
一个正数算1分, 问最多可以得到多少分? 
Input: nums = [2,-1,0,1,-3,3,-3]
Output: 6
Explanation: We can rearrange the array into nums = [2,3,1,-1,-3,0,-3].
prefix = [2,5,6,5,2,2,-1], so the score is 6.
It can be shown that 6 is the maximum score we can obtain.
- 思路: 
'''
class Solution:
    def get_score(self, nums):
        res = 0 
        for n in nums:
            if n>0:
                res += 1
        return res

    def maxScore(self, nums: List[int]) -> int:
        nums=sorted(nums, key=lambda x:-x)
        # print("sorted nums ", nums)
        prefix_sums =   list(accumulate(nums))
        # print(prefix_sums)

        sc = self.get_score(prefix_sums)
        # print("max score = ", sc)
        return sc

so = Solution()
so.maxScore([2,3,1,-1,-3,0,-3])
so.maxScore([-2,-3,0])
so.maxScore([-2 ])
so.maxScore([2 ])

exit(0)
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