'''
动态规划问题
'''
from collections import Counter
import collections
from typing import List
from functools import lru_cache
import heapq
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
- https://leetcode.com/problems/best-team-with-no-conflicts/
- 1626. Best Team With No Conflicts (Medium)
- 问题:  
你是一个球队教练, 要举行一个比赛, 需要召集一批得高分的球员.
输入两组数据, 分别代表球员的分数和年纪数组, 选出能够得到最高分的组合.
不能有冲突: 年纪小的球员分数大于年纪大的球员分数
- 思路:
应该是个动态规划, 根据 年纪做个排序, 得出分数和年纪的关系数据. 然后从年纪低的开始累加分数, 若当前年纪大于前一个年纪, 且分数大于等于前一个球员分数, 则累加到结果,
若当前年纪大于前一个球员年纪, 但是分数更小, 展开一个新的分支, 从当前球员开始累加

    '''
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        age_score   =   sorted(zip(ages, scores), key= lambda x: x[0])
        max_score   =   -1
        print(age_score, len(age_score))
        
        def make_best_team(cur_score:int, player_id:int, pre_age, pre_score):
            nonlocal age_score, max_score
            
            if player_id < len(age_score):
                # print(f"cur id = {player_id}")
                player_age, player_score    =   age_score[player_id]
                
                # 前一个队员年纪小 且分数小于等于
                if pre_age <= player_age and pre_score <= player_score:
                    make_best_team(cur_score+player_score, player_id+1,
                        player_age, player_score)
                    # cur_score   +=  player_score
                    # max_score   =   max(max_score, cur_score)
                # 前一个队员年纪小 但是分数确大于当前的, 这两种情况
                elif pre_age < player_age and pre_score > player_score:
                    make_best_team(cur_score, player_id+1,
                        pre_age, pre_score)
                    make_best_team(player_score, player_id+1,
                        player_age, player_score)
                else:
                    make_best_team(cur_score+player_score, player_id+1,
                        player_age, player_score)
            
            else:
                # print("id = {} 计算最大分数 {} {}",player_id, max_score, cur_score)
                max_score   =   max(max_score, cur_score)
        
        make_best_team(0,0,0,0)
        return max_score

    '''
- https://leetcode.com/problems/remove-stones-to-minimize-the-total/
- 1962. Remove Stones to Minimize the Total (medium)
- 问题:  
输入一组数字, 每一个表示一堆石头的个数, 输入一个数字k, 完成以下操作k次:
选中某一堆石头, 数量除以2(向右取整), 同一堆可以被多次除以2
要使得最后石头总数最小, 问最小的总数是多少.
- 思路:
用最大堆即可解决. python 是最小堆需要转化
Beats 71.19%
    '''
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-i for i in piles]
        heapq.heapify(piles)
        while k:
            heapq.heappushpop(piles, piles[0] // 2)
            k -= 1
        return -sum(piles)

        # large   =   []
        # for q in piles:
        #     heapq.heappush(large, -q)
        
        # # heapq.heapify(piles)
        # while k > 0:
        #     k   -=  1
        #     quantity    =   -heapq.heappop(large)
        #     print("pop {}".format(quantity))
        #     quantity    =   math.ceil(quantity/2)
        #     print("push {}".format(quantity))
        #     heapq.heappush(large, -quantity)
        # print(large)
        # return  -sum(large)

    '''
- https://leetcode.com/problems/jump-game/
- 55. Jump Game(medium)
- 问题:  
输入一组数字, 每个数字代表从当前索引最多可以跳多少步, 问输入数组,能否跳到最后一个索引: Input: nums = [2,3,1,1,4]
Output: true: 第0个索引跳1步, 第1个索引跳3步.
- 思路:
从最后一个索引往前搜索, 找出所有可以跳到最后一个索引的数字,
把他们加入二轮搜索
This is a very Philosophical problem: even you have the smallest jump every index (every day), you will reach the last index (destination) no matter what (need no algorithm to figure out). But once you have a zero in the way, you may have troubles.
    '''
    def canJump(self, nums: List[int]) -> bool:
        if nums[0] == 0 and nums.__len__() > 1:
            return False
        reach_end   =   []
        for idx, jump in enumerate(nums[:-1]):
            if idx + jump >= len(nums) - 1:
                reach_end.append(idx)
                # can jump from index 0 to end
                if idx == 0:
                    return  True
        for idx in reach_end:
            print(idx, nums[idx])
        if reach_end:
            for idx in reach_end:
                print("into recursive")
                r=self.canJump(nums[:idx])
                if r :
                    return r
        
        return  False
    '''
- https://leetcode.com/problems/longest-common-subsequence/
- 1143. Longest Common Subsequence
- 问题:  
输入两个字符串, 返回他们相同的最长子序列的长度. 子序列是在不改变字符相对顺序的情况下, 删除一些字符得到的子串. abcde-> ace
- 思路1
取出短的字符串, 生成它的所有子序列, 然后从最长到最短开始校验.
编写生成所有子序列函数 和 子序列校验函数.
- 大神思路
类似之前机器人从左上角走到右下角, 有多少种走法. m j n 两个字符串长度, 构成一个 矩阵:
i 行 j 列
  a b c d e
b 0 1 1 1 1
c 0 1 2 2 2 
e 0 1 2 2 3   => 3 
- 大神思路2
同样也是机器人的思路, 搜索一个路径, 若符合则返回1, 不符合则同时向两个字符串移动
Beats 77.77%
    '''
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def findMax(i, j):
            if memo[i][j] == -1:
                if i == n1 or j == n2: 
                    res = 0
                else:
                    if text1[i] == text2[j]:
                        res =  1 + findMax(i+1, j+1)
                    else:
                        res =  max(findMax(i+1, j), findMax(i, j+1))
                memo[i][j] = res
            return memo[i][j]

        n1, n2 = len(text1), len(text2)
        memo = [[-1 for j in range(n2+1)] for i in range(n1+1)]
        return findMax(0, 0)
        # return matrix[text2.__len__()][text1.__len__()]
        len_    =   max(text1.__len__(), text2.__len__())
        matrix  =   [[0] * (len_+1)] * (len_ + 1 )
        #-------- 矩阵大小必须取更大的那个, 因为循环的时候 长的字符串 会使得 短的字符串访问矩阵溢出 .
        print("s1={} s2={}".format(text1, text2))
        print("j len {}".format(len(matrix[0])))
        print("i len {}".format(len(matrix)))
        
        for i in range(text2.__len__()):
            for j in range(text1.__len__()):
                matrix[i+1][j+1]    =  matrix[i][j] + 1 \
                    if text1[j] == text2[i] else max(matrix[i][j+1], matrix[i+1][j])
            print(matrix)
        return matrix[text2.__len__()][text1.__len__()]
        # for i in range(text1.__len__()):
        #     for j in range(text2.__len__()):
        #         print("\ncur: ci={} cj={}".format(text1[i], text2[j]))
        #         if text1[i] == text2[j]:
        #             matrix[i+1][j+1]    =  matrix[i][j] + 1
        #             print("j={},i={} matrix[j+1][i+1]={}".format(text2[j],text1[i], matrix[j+1][i+1]))
        #         else:
        #             matrix[i+1][j+1]    =    max(matrix[i][j+1], matrix[i+1][j])
        #             print("max {} {}".format(matrix[i][j+1], matrix[i+1][j]))
        #     print(matrix)
                # matrix[i+1][j+1]    =  matrix[i][j] + 1 \
                #     if text1[i] == text2[j] else max(matrix[i][j+1], matrix[i+1][j])
                    
                # print("j={},i={} matrix[j+1][i+1]={}".format(text2[j],text1[i], matrix[j+1][i+1]))
        # print(matrix)
        return matrix[len_][len_]
        # return matrix[text2.__len__()][text1.__len__()]
    '''
- https://leetcode.com/problems/house-robber/
- 198. House Robber(medium)
- 问题:  
抢劫一个街道上的房子, 每个房子有一定的现金, 但是每个房子有警报, 若同时抢劫相邻的两个房子会报警, 问最多可以抢多少钱.
- 思路
和斐波那契数列有关系? 抢了第一家就不能抢第二家, 抢第二家就不能抢第1和3家.  一共n家, 找出所有的 n-1 家. 
得出递推方程 f(n) 表示n家能抢的最多钱, house[n] 表示第 n 家有多少钱
f(1) = house[1]
f(2) = max( f(1), house[2])
f(3) = max( f(2), house[3]+f(1))
f(4) = max( f(3), house[4]+f(2))
f(5) = max( f(4), house[5]+f(3))
Beats 92.6%
    '''
    def rob(self, nums: List[int]) -> int:
        # within 2 house, return the max one
        if nums.__len__() < 3:
            return max(nums)
        f_1 =   nums[0]
        f_2 =   max(f_1, nums[1])
        f_cur   =   f_2
        for i in range(2, nums.__len__()):
            f_cur   =   max(f_2, nums[i] + f_1)
            f_1     =   f_2
            f_2     =   f_cur
        return f_cur
    '''
- https://leetcode.com/problems/climbing-stairs/
- 70. Climbing Stairs(easy)
- 问题:  
跳楼梯, 一次跳一阶或两节, 跳到 n 阶有多少种跳法
- 思路
青蛙跳楼梯, 若第一次跳1阶, 剩下 n-1阶的跳法为 f(n-1)+1, 若第一次跳2阶,
剩下 n-2 阶跳法为 f(n-2) +1, 因此 n 个台阶, 是 f(n) = f(n-1) + f(n-2)
Beats 74.57%
'''
    def climbStairs(self, n: int) -> int:
        if n < 3:
            return n
        a,b = 1,2
        for i in range(2, n):
            b  = a + b
            a  = b - a 
        return b
    
    @lru_cache(1000)
    def climbStairs(self, n):
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n-1) + self.climbStairs(n-2)

    '''
    # https://leetcode.com/problems/decode-ways/
    # 91. Decode Ways
    问题: 假设有映射方式: A-Z 映射为 1-26.
    输入一串数字, 返回可能的解码方式. 如输入 226, 返回 3. 因为226可以解码为(2,2,6); (22,6); (2,26)
    思路1: 从前往后计算
    思路2: 动态规划, 从后往前计算
    Runtime: 89 ms, faster than 5.21% of Python3 online submissions for Decode Ways.
    Memory Usage: 13.8 MB, less than 80.35% of Python3 online submissions for Decode Ways.
    '''
    def numDecodings(self, s: str) -> int:
        cur, p, pp  =   0,1,1
        pc          =   ''  # 保存前一个字符
        for c in range(1, s.__len__()+1):
            # print(f"index={c} char={s[-c]} p= {p} pp= {pp}")
            if s[-c] == '0':
                cur     =   0
            else:
                cur     =   p
            # 若当前字符是1, 则前一个字符必须非空才能加上 pp
            # 若当前字符是2, 则前一个字符必须小于 7 才能加pp
            if  s[-c] == '1' and \
                pc != '' or \
                s[-c] == '2' and \
                pc !='' and \
                pc <'7':
                cur +=  pp
            pc      =   s[-c]
            pp      =   p
            p       =   cur
            # print(f"cur={cur}")
            
        return  cur
