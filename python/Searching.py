'''
搜索类算法
'''
from collections import Counter
import collections
from typing import List
from functools import lru_cache
import heapq

def guess(self, x):
    pass
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
- https://leetcode.com/problems/daily-temperatures/
- 739. Daily Temperatures(medium)
- 问题:  
输入一组温度, 返回数组, 每一个表示在 第 i 天需要等待多少天才能得到更温暖的温度.
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
73->74 等待1天
74->75 等待1天
75->76 等待4天 ...
- 思路1:
直接遍历即可. 遇到大的直接超时了 ....
- 思路2:
其实存在重复的计算, 比如 75,71,69,72,76. 75 < 76 得出这区间的数都是小于76,
那么这区间的数字的结果, 搜索范围就不用超出 76 这个数字了, 在这个范围内搜索即可.

- 思路3: 最大堆
初始化一个 cur_max 表示当前的最高温度, 把输入温度组合他们的第n天, 变成一个最大堆. 初始化结果全部为0 
每次从最大堆取一个值出来, 和当前最高气温做对比, 计算时间差.
想法还可以, 可惜是错的. 会丢失数据, 导致结果错误.
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # 思路2 根据前一轮计算结果
        ret     =   []
        for i, temp in enumerate(temperatures):
            has_warmmer =   False
            count    =   temperatures.__len__()  -   i - 1
            # 前一天的气温大于当前的, 则前一天的结果可以被复用
            if i > 0 and \
                temperatures[i-1] > temp:
                count = ret[i-1] - 1
            j = i+1
            # print("[+]i= {} tmpe = {} count = {}".format(i, temp,count))
            while count > 0:
                # print("j= {} tmp= {} cur_tmp = {}".format(j, 
                # temperatures[j], temp))

                if j<temperatures.__len__() and temperatures[j] > temp:
                    ret.append(j-i)
                    has_warmmer =   True
                    break
                j       +=  1
                count   -=  1


            # for j, temp1 in enumerate(temperatures[i+1:size]):
            #     if temp1 > temp:
            #         ret.append(j+1)
            #         has_warmmer =   True
            #         break
            if not has_warmmer:
                ret.append(0)
        return  ret
        # 思路3 最大堆
        # ret     =   [0] * temperatures.__len__()
        # cur_max =   None
        # large_heap  =   []
        # for i,temp in enumerate(temperatures):
        #     heapq.heappush(large_heap, (-temp,i))
        
        # for x in range(len(temperatures)):
        #     item    =   heapq.heappop(large_heap)
        #     print(item)
        #     #  item = (-76, 6)
        #     if not cur_max:
        #         cur_max =   item
        #         continue
        #     # 第 i 天要等待的天数
        #     wait_days   =   cur_max[1]  -   item[1]
        #     if wait_days    > 0:
        #         ret[item[1]]    =   wait_days
        #     print("{} 天是 {} 度, 要等待 {} 天 达到 {} 度".format(item[1], item[0], wait_days, cur_max[0]))
        #     cur_max =   item
        # return ret
            

        # 思路1 超时
        # ret     =    []
        # for i, temp in enumerate(temperatures):
        #     has_warmmer =   False
        #     for j, temp1 in enumerate(temperatures[i+1:]):
        #         if temp1 > temp:
        #             ret.append(j+1)
        #             has_warmmer =   True
        #             break
        #     if not has_warmmer:
        #         ret.append(0)
        
        # return ret

