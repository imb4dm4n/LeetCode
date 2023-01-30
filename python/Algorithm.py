'''
未分类的算法
'''
from collections import Counter
import collections
from typing import List
from functools import *
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
- https://leetcode.com/problems/n-th-tribonacci-number/
- 1137. N-th Tribonacci Number (easy)
- 问题:  
三波纳气数列的定义:T0=0,T1=1,T2=1, T(n+3)=T(n) + T(n+1) + T(n+2) 其中n>=0.
输入 n 返回 T(n) 的值
- 思路:
斐波那契数列的累加 T(3)=T(0)+T(1)+T(2); T(4)=T(1)+T(2)+T(3);
变量传播
Beats 95.85%
    '''
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        a,b,c,d = 0,1,1,0
        for i in range(n-2):
            d = a + b + c
            a = b
            b = c
            c = d
        return d
    '''
- https://leetcode.com/problems/flip-string-to-monotone-increasing/
- 926. Flip String to Monotone Increasing (medium)
- 问题:  
输入一个字符串包含0和1, 要求用最小的变化次数, 让字符串成为单调递增的.
可以把0 变成1 也可以把1变成0, 
Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
- 思路:
贪心算法:
    1. 把1后面的0全变成1, 把前面的1变成0
    2. 把所有1变成0
    3. 把所有0变成1
    找出最小的那个
    4. 可能输入的本身就是单调递增呢
    '''
    def minFlipsMonoIncr(self, s: str) -> int:
        def is_mono_incr(inp:str):
            t   =   0
            for c in inp:
                if ord(c) - t < 0:
                    return False
                t   =   ord(c)
            return True
        if is_mono_incr(s):
            print("{} is_mono_incr".format(s))
            return 0
        # 统计字符串中的 0 和 1 的个数, 这样可以快速知道 贪心算法后两个的结果
        count_zero, count_one,count_flip   =   0,0,0
        def min_flip(inp:str):
            raw     =   [ord(c) for c in inp]
            mut     =   sorted(raw)
            count       =   0
            for i, x in enumerate(mut):
                if x != raw[i]:
                    count   +=  1
            print("{} need {}".format(s, count))
            return count

        replace_zero    =   True
        replace_one     =   False
        # search_zero     =   False
        # search_one      =   True
        for c in s:
            if c == '0':
                count_zero  +=  1
            elif c == '1':
                count_one   +=  1
            # if replace_zero and c == '1':
            #     replace_zero    =   False
            #     replace_one     =   True
            # elif replace_zero and c =='0':
            #     count_flip  +=  1

            # if replace_one and c == '1':
            #     pass
            # elif replace_one and c == '0':
            #     count_flip  +=  1

        t   =   []
        if count_zero:
            t.append(count_zero)
        if count_one:
            t.append(count_one)
        count_flip  =   min_flip(s)
        if count_flip:
            t.append(count_flip)
        print("{} find min in {}".format(s, t))
        return min(t)

    '''
- https://leetcode.com/problems/insert-interval/
- 57. Insert Interval(medium)
- 问题:  
输入一个数组 intervals , 每一项是不重叠的任务开始和结束时间intervals[i] = [starti, endi] . 并且以开始时间排序了, 再输入一个 开始时间和结束时间, 插入到 intervals 中, 若发生了重叠, 那么合并他们为一个:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
- 思路:
一维数组的重叠判断: (a,b) & (c,d) 如何判断重叠? 
1.(a,b) <= (c,d): c <= b && b <= d
2.(a,b) >= (c,d): a <= d && d <= b
3.本质就是, 一个范围 X(a,b) 的上界必须大于等于另一个范围 Y(c,d) 的下界 : b >= c. 这样就能保证重叠. 但是具体是怎样的覆盖情况, 还需要判断.
    1. b >= c && b >= d : 那么 X 范围完全覆盖 Y
    2. b >= c && b < d  : 那么 X 范围和 Y 存在交集, 上界是 Y的d
Beats 87.16%
    '''
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        c, d            =     newInterval
        merge_offsets   =     []        # 存储需要合并的 时间区间 下标 列表
        insert_index    =   -1
        for i,(a, b) in enumerate(intervals):
            # 情况 1
            if c <= b and b <= d:
                merge_offsets.append(i)
                print("情况1 ",a,b)
            
            # 情况 2
            elif a <= d and d <= b:
                merge_offsets.append(i)
                print("情况2 ", a,b)
            
            # 没有重叠
            elif b < c:
                insert_index    =   i + 1
        
        # 1. 不需要合并, 找个合适的位置插入
        if merge_offsets.__len__() == 0:
            # print("insert {} {}".format(insert_index, newInterval))
            # 小于第一个
            if insert_index == -1:
                intervals.insert(0, newInterval)
            else:
                intervals.insert(insert_index, newInterval)
            return  intervals
        
        # 2. 需要合并
        lower   =   min(c, intervals[merge_offsets[0]][0])
        higher  =   max(d, intervals[merge_offsets[-1]][1])
        to_merge    =   [lower, higher]
        
        # 若不修改原始数组
        # r       =   []
        # for i , p in enumerate(intervals):
        #     if i in merge_offsets:
        #         continue
        #     r.append(p)
        # r.insert(merge_offsets[0], to_merge)

        # 删掉需要合并的
        for i in range(len(merge_offsets)):
            intervals.pop(merge_offsets[0])
        intervals.insert(merge_offsets[0], to_merge)

        # print(merge_offsets, " to merge ", to_merge)
        return intervals


    '''
- https://leetcode.com/problems/gas-station/
- 134. Gas Station(medium)
- 问题:  
输入一组数表示第i个加油站的油量, 另一组数字表示从i到i+1加油站的耗油量, 问一开始没有油, 从哪个加油站开始出发, 可以完成一次旅行.
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
- 思路:
[1,2,3,4,5]
[3,4,5,1,2]
起始点的加油站油量必须大于等于它到下一个加油站的耗油量.
gas_left 表示当前剩余油量, gas_can_fill 表示当前可以增加的油量,
gas_2_next_station 表示到下一个加油站的耗油量, start_station 表示出发点,
cur_station 表示当前所处的坐标
其实题目已经是答案了, 只要顺着把代码实现, 找出所有可能的出发点, 并对每一个可能都进行验证即可. 超时了 ... 

- 思路2 (其实一轮trip没必要想到环, 因为可以想象把前面的移动到后面 )
其实存在冗余的计算, 比如从 i 到 j 的加油站, 是无法到达的, 那么 其实从 i+1 到 j 都是不用去计算的. 
因为 j-1 到 j 肯定是需要额外的油, 但是从 i 到 j-1 剩余的油 加上j-1的油是过不到j的. 
虽然 i 到 j-1 有额外剩余, 但是 j-1 到 j 就不够了, 所以从 i+1 开始到 j 剩余的油肯定也是不够的. 
Beats 71.32%
    '''
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_surplus, surplus, start_pos  =   0,0,0
        for i in range(gas.__len__()):
            total_surplus   +=  gas[i]  -   cost[i]
            surplus +=  gas[i]  -   cost[i]
            # 盈余为小于 0 , 说明 从 0 到当前是无法完成的, 因此 移动起始偏移
            if surplus  < 0:
                start_pos   =   i   +   1
                surplus     =   0
        
        return -1 if total_surplus < 0 else start_pos
        
        # start_poss   =   []  # 保存所有可以作为出发点的起始偏移
        # for pos, cur_gas in enumerate(gas):
        #     # 油量大于等于到下一站的耗油量
        #     if cur_gas and cur_gas >= cost[pos]:
        #         start_poss.append((pos, cur_gas))
        
        # start_poss.sort(key= lambda x:(-x[1]))
        
        # def can_travel_around(start_pos):
        #     '''
        #     验证能否从 start_pos 旅游一圈
        #     '''
        #     # 先移动到下一个加油站
        #     gas_left, cur_station   =   gas[start_pos] - cost[start_pos], (start_pos + 1) % gas.__len__()
        #     while cur_station != start_pos and gas_left >=0:
        #         # 加满油
        #         gas_left    +=  gas[cur_station]
        #         # 尝试移动到下一个加油站
        #         if gas_left >= cost[cur_station]:
        #             gas_left    -=  (cost[cur_station])
        #             cur_station =   (cur_station+1) % gas.__len__()
        #             continue
        #         break
            
        #     if cur_station == start_pos:
        #         return  True
            
        #     return False

        # for pos in start_poss:
        #     # print("can travel from post {} ?".format(pos))
        #     if can_travel_around(pos[0]):
        #         return pos[0]
        
        # return -1

    '''
- https://leetcode.com/problems/maximum-ice-cream-bars/
- 1833. Maximum Ice Cream Bars(medium)
- 问题:  
输入一组数字表示每个冰激凌的价格, 男孩有 n 个硬币, 问它最多可以买多少个冰激凌.
Input: costs = [1,3,2,4,1], coins = 7
Output: 4 (The boy can buy ice cream bars at indices 0,1,2,4 for a total price of 1 + 3 + 2 + 1 = 7.)
- 思路1:
直接排序以下, 然后从头开始累加, 找到小于等于 coins 的个数即可.
Beats 24.34%
- 思路2:
堆排序, 然后累加, 找到小于 coin的
Beats 46.86%
- 思路3:
排序, 做减法. Beats 75.24%
    '''
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        n = 0
        for cost in costs:
            if cost > coins:
                return n 
            n += 1
            coins -= cost
        return n
        # 思路2
        heapq.heapify(costs)
        total_cost  =   0
        count   =   0
        while costs.__len__ () > 0:
            if total_cost  + costs[0] > coins:
                break
            total_cost  +=  heapq.heappop(costs)
            count   +=  1
        return count
        # 思路1:
        # costs.sort()
        # total_cost  =   0
        # for i, price in enumerate(costs):
        #     if total_cost   +   price > coins:
        #         # 因为 i 是从 0 开始计数, 因此不用再 - 1 了
        #         return i  if i > 0 else 0
        #     total_cost  +=  price

        # # 可以买所有冰激凌
        # return costs.__len__()
    
    '''
- https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/
- 452. Minimum Number of Arrows to Burst Balloons (medium)
- 问题:  
输入一组气球在 x 轴上的坐标范围, 找出最少的剑向y轴方向射出, 把所有气球打爆需要多少剑.
^y
|
|     (气球  )
|  (气球  )
|--------------> x 这里只要一只剑可以射爆两个气球
Input: points = [[10,16],[2,8],[1,6],[7,12]]
Output: 2
Explanation: The balloons can be burst by 2 arrows:
- Shoot an arrow at x = 6, bursting the balloons [2,8] and [1,6].
- Shoot an arrow at x = 11, bursting the balloons [10,16] and [7,12].
- 思路:
其实是求交集能够让更多的x坐标重叠.(a,b) (c,d) 若 b >= c && a <=d
    '''
    
    '''
- https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
- 2244. Minimum Rounds to Complete All Tasks(medium)
- 问题:  
输入一组数字代表任务难度, 每次可以完成相同难度的任务2个或3个, 问最少通过多少轮可以完成任务. 若无法完成, 则返回-1
- 思路:
统计每个难度等级的任务数量, 他们必须能够被2 或 3 整除, 尽可能用3去整除, 不行再用2, 最后如果余数为1 则返回-1
- 思路2:
任何一个数字都可以表达为: n >= 0
3n + 1 = 3(n-1) + 2 + 2 = n + 1 次
3n + 2 = n + 1 次
因此可以表达为 (x+2) // 3
Beats 84.92%
    '''
    def minimumRounds(self, tasks: List[int]) -> int:
        m_task  =   Counter(tasks)
        def get_min_rounds(count):
            '''
            count 表示任务数量, 计算最少完成 count 的轮次
            不同方式有不同的结果: 输入8可以是两次3和一次2, 也可以是4次2.
            '''
            if count == 1:
                return -1
            if count % 3 == 0:
                return count // 3
            
            return count // 3 + 1
        
        n   =   0
        for k,c in m_task.items():
            r   =   get_min_rounds(c)
            # print("num = {} c={} r={}".format(k, c, r))
            if r == -1 :
                return -1
            n   +=  r
        return  n
    
    '''
- https://leetcode.com/problems/find-pivot-index/?envType=study-plan&id=level-1
- 724. Find Pivot Index(easy)
- 问题:  
输入一组数字, 找到中间索引, 以此索引左边的数的和 等于 右边数的和.
如  [1,7,3,6,5,6] => 3 因为 1+7+3 = 5+6
边界条件: 若索引是左边的边界, 那么左边的和为0, 同理适用右边边界
- 思路 1 
先计算数组中间索引, 然后求左边的和是否等于右边的和.
若 left_sum < right_sum 那么 pivot + 1 
否则 pivot -1
错了. 这个数组不是排序的数组, 因此修改 pivot 的方向并不能增大或减小他们的和.
因此只能暴力的穷举了.
- 思路2
从第一个索引开始到倒数第二个索引, 开始求和
Runtime: 9799 ms, faster than 5.01% of Python3 online submissions for Find Pivot Index.
Memory Usage: 15.2 MB, less than 49.09% of Python3 online submissions for Find Pivot Index.
- 思路3
先求总和, 然后从左往右开始分别做减法和加法
    '''
    def pivotIndex(self, nums: List[int]) -> int:  
        left_sum, right_sum =   0,  sum(nums)
        for idx, num in enumerate(nums):
            right_sum    -=  num    # 因为是开区间
            if left_sum == right_sum:
                return idx
            left_sum    +=  num
        return -1
            
        # for i in range(0, len(nums)):
        #     if sum(nums[:i]) == sum(nums[i+1:]):
        #         return i
        # return -1
        
        # pivot   =   int(nums.__len__() / 2)
        # left_sum    =   sum(nums[:pivot])
        # right_sum   =   sum(nums[pivot+1:])
        # print(f"pivot {pivot}")
        # while left_sum != right_sum and \
        #     pivot >=0 and pivot < nums.__len__():
        #     is_left_small   =   False
        #     if left_sum < right_sum:
        #         pivot   +=  1
        #         is_left_small   =   True
        #     else:
        #         pivot   -=  1
        #     left_sum    =   sum(nums[:pivot])
        #     right_sum   =   sum(nums[pivot+1:])
        #     if is_left_small and left_sum > right_sum or \
        #         not is_left_small and left_sum < right_sum:
        #         break
        
        # if left_sum ==  right_sum:
        #     return pivot
        
        # return -1 
        

    '''
- https://leetcode.com/problems/sort-characters-by-frequency/
- 451. Sort Characters By Frequency(medium)
- 问题:  
输入一个字符串s, 以字符出现次数的降序, 输出每个字符. 比如输入
abcaab -> aaabbc
- 思路 1
直接 Counter计数, 然后来个 sort, 最后遍历一遍乘出来即可
Runtime: 87 ms, faster than 56.10% of Python3 online submissions for Sort Characters By Frequency.
Memory Usage: 15.3 MB, less than 49.59% of Python3 online submissions for Sort Characters By Frequency.
    '''
    def frequencySort(self, s: str) -> str:
        # r       =   ''
        # for c in sorted(
        #     Counter(s).items(),
        #     key= lambda x: -x[1]
        #     ):
        #     r += c[0] * c[1]
        # return r

        c_counter   =   [0] * 127
        for c in s:
            c_counter[ord(c)]   +=  1
        r           =   ''
        while len(r) != s.__len__():
            max_    =   0
            c = ''
            for i in range(127):
                if c_counter[i] > max_:
                    max_    =   c_counter[i]
                    c = chr(i)
            c_counter[ord(c)]=0
            r += c * max_
        return r
                
    '''
- https://leetcode.com/problems/unique-number-of-occurrences/solution/
- 1207. Unique Number of Occurrences(easy)
- 问题:  
输入一组数字, 判断每个数字出现的次数, 是否唯一. 不唯一返回False
- 思路 
直接Counter计数, 然后 set 一下对比长度
Runtime: 33 ms, faster than 97.46% of Python3 online submissions for Unique Number of Occurrences.
Memory Usage: 14 MB, less than 34.11% of Python3 online submissions for Unique Number of Occurrences.
    '''
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts=Counter(arr).values()
        return set(counts).__len__() == counts.__len__()
    '''
- https://leetcode.com/problems/valid-sudoku/
- 36. Valid Sudoku(medium)
- 问题:  
输入一个 9X9 的九宫格, 验证存在数字的格子是否满足以下条件:
每一行没有重复的数字, 每一列没有重复的数字, 每3x3小个的九宫格
没有重复的数字.

- 思路 
每一行的数字加入到一个数组, 然后做 set 验证长度是否相等;
每一列的数字加入到数组, 做set后验证长度;

    '''
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        pass
    '''
- https://leetcode.com/problems/perfect-squares/
- 279. Perfect Squares(medium)
- 问题:  
输入一个数字n, 返回最少需要的 完美方形数字的个数, 他们的和为n.
完美方形数字指的是可以被某个数字乘以自身得到的, 如1/4/9/16...

- 思路 
根据n的值, 生成到大于等于n的 完美方形数字列表.
然后从后往前加, 直到发现一组满足的数字.

    '''
    def numSquares(self, n: int) -> int:
        perfect_squares     =   [1]
        square_base  =   1
        cur_square   =   1
        while cur_square    <   n:
            square_base+=1
            cur_square  =   square_base*square_base
            perfect_squares.append(cur_square)
        

    '''
- https://leetcode.com/problems/rectangle-area/
- 223. Rectangle Area(medium)
- 问题:  
输入两对坐标(ax1, ay1) (ax2, ay2),(bx1, by1)  (bx2, by2) 表示两个矩阵, 求他们占用的大小. (可能重叠)
- 思路 
y轴的重叠区间, 可以判断他们是否在同一个高度.
x轴的重叠区间, 可以判断他们是否重叠.
通过 range 输出两对 set, 每一对set表示 x 轴的 坐标集合, y 轴的坐标集合.
若他们没有交集, 则返回他们的大小的和.
若有交集, 计算他们大小的和后, 减去重叠部分.
Runtime: 404 ms, faster than 5.30% of Python3 online submissions for Rectangle Area.
Memory Usage: 31.9 MB, less than 5.43% of Python3 online submissions for Rectangle Area.
    '''
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        import numpy as np
        set_ax  , set_ay, set_bx, set_by = set(np.arange(ax1, ax2)),\
            set(np.arange(ay1, ay2)),set(np.arange(bx1, bx2)),\
                set(np.arange(by1, by2))
        has_collision = 0
        collision_x     =   (set_bx & set_ax)
        collision_y     =   (set_ay & set_by)
        if collision_x and collision_y:
            has_collision       =   len(collision_x) * len(collision_y)

        
        a = (ax2- ax1) * (ay2 - ay1)
        b = (bx2- bx1) * (by2 - by1)
        return  a + b - has_collision

    '''
- https://leetcode.com/problems/guess-number-higher-or-lower/
- 374. Guess Number Higher or Lower(easy)
- 问题:  
玩一个游戏,输入一个数字n, 机器随机选一个数字, 然后
你去猜测它选了哪个, 可以调用一个 函数获取选中的数字是
大于(返回-1)还是小于(1) 它选的.
- 思路 
    '''
    def guessNumber(self, n: int) -> int:
        while True:
            i = int(n/2)
            g_result    =   guess(i)
            if  g_result== 0:
                return i
            elif g_result == -1:
                # i 太大了 选取左半部分
                n = i 
                # i -= 1
            else:
                n += i
            
            
    '''
- https://leetcode.com/problems/where-will-the-ball-fall/
- 1706. Where Will the Ball Fall(medium)
- 问题:  
输入一个 mxn的2D矩阵.有n个盒子, 通向底部, 若盒子的值为1, 则朝右开放, 否则朝左开放. 请问从上面每一个格子丢小球, 对应会从哪列出来. 若出不来, 用-1表示
- 思路
构成通道必须相邻的盒子值是相同的, 否则构成死路.
每一个入口对应一个出口 或 死路.
输入入口索引, 判断当前层的出口通道, 若正好是出口通道, 则移动到下一层;
同时修改入口索引为选择的出口通道.
    '''
    def dfs_next_level(self, grid: List[List[int]], entry:int, level:int) -> int:
        '''
        深度遍历 grid. 
        :param      grid        矩阵
        :param      entry       入口的索引
        :param      level       当前处于第几行
        :returns    当前层对应的出口索引
        '''
        if level == len(grid) or \
            entry >= len(grid[0]) or \
            entry < 0:
            return -1
    
        row_data    =   grid[level] # 取出一层
        # 边界处理: 遇到最右边的入口
        if entry == len(row_data) - 1:
            if row_data[entry] == 1 or \
                row_data[entry]== -1 and entry-1>-1 and\
                row_data[entry-1] == 1:
                return -1
            return self.dfs_next_level(grid, entry-1, level+1)

        # 判断当前层对应的入口是否有出口, 有则进入下一层, 否则返回 -1
        if entry+1 < len(row_data):
            if row_data[entry] == row_data[entry+1]:
                next_entry  = entry + 1 if row_data[entry] == 1 else entry -1
                # 到达最后一层, 找到出口返回
                if level+1 == len(grid):
                    return next_entry
                return self.dfs_next_level(grid, next_entry, level+1)
            return -1
        return -1
    
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ret     =   []
        for i in range(len(grid[0])):
            # 从每一个入口进入
            ret.append(
                self.dfs_next_level(grid, i, 0)
            )
        return  ret

    '''
- https://leetcode.com/problems/toeplitz-matrix/
- 766. Toeplitz Matrix(easy)
- 问题:  
输入一个 mxn的矩阵,  若矩阵是 Toeplitz 则返回true: 即每个坐上到右下的对角线的元素是一样的.
- 思路
判断当前节点是否有下一行和下一列, 若存在则直接计算对角线的坐标, 进行对别. 只要有一项不符合, 立刻返回 false
Runtime: 92 ms, faster than 91.65% of Python3 online submissions for Toeplitz Matrix.
Memory Usage: 13.8 MB, less than 78.65% of Python3 online submissions for Toeplitz Matrix.
    '''
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        for x in range(0, matrix.__len__()-1):
            for y in range(0, matrix[0].__len__()-1):
                # find the diagonal element
                # print(f"[{x}][{y}]")
                if matrix[x][y] != matrix[x+1][y+1]:
                    return False
                        
        return True


    '''
- https://leetcode.com/problems/earliest-possible-day-of-full-bloom/
- 2136. Earliest Possible Day of Full Bloom(hard)
- 问题:  
一朵花播种需要耗时, 生长需要耗时. 输入一组种子的播种耗时和生长耗时, 找出最短的时间内可以让所有种子开花的播种顺序, 返回耗时.
- 思路: (类似apk的解析研判 和 入库操作, 入库可以与解析并行, 但是解析之间不能并行, 是串行的; 但是入库与入库之间是可以并行的.)
观察到: 
a.无论时间怎么短, 种花的耗时是必须的, 因此最短时间至少是所有种花时间的总和.(因此找出一个最优种花顺序, 然后找到开花时间最长的那个耗时, 就是最短耗时. 因为种花顺序已经是最优了)
b.耗时取决于最后一个种子播种时间和最后一个种子开花时间
1. 播种耗时是无法并行的, 所以需要尽可能减少对生长耗时的阻塞?
2. 为了尽可能的并行生长, 需要根据生长耗时降序排序.
Runtime: 1760 ms, faster than 96.77% of Python3 online submissions for Earliest Possible Day of Full Bloom.
Memory Usage: 34.8 MB, less than 39.35% of Python3 online submissions for Earliest Possible Day of Full Bloom.
    '''
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ret         =   0
        plant_day   =   0   
        # 生长是可以并行的, 所以把生长耗时长的任务先做
        # 剩下就是慢慢的种地, 找到耗时最长的重地?
        for plant, grow in sorted(zip(plantTime, growTime), key=lambda x: -x[1]):
            plant_day    +=  plant    # 
            ret     =   max(ret, plant_day+grow)
            pass
        return      ret
        
    '''
- https://leetcode.com/problems/image-overlap/
- 835. Image Overlap
- 问题:  
输入两个图片, 以二进制表示, 每个单元值为1或0. 通过对一张图片中的所有1做 翻译 操作, 
即把所有的1同时向上/下/左/右移动(超出边界的1被抹去), 最后计算这两种图片最大的1重叠个数.
- 思路:
最优的情况, 第一张图片移动后和第二张完全一样.
定义一个翻译函数, 把输入的矩阵根据方向移动1
统计每一行有多少个1. 把
    '''
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        pass
    
    '''
- https://leetcode.com/problems/contains-duplicate-ii/
- 645. Set Mismatch(easy)
- 问题:  
输入一组数从1-n, 其中一个数重复了, 找出并返回它和丢失的那个. ie: [1,2,2,4] => [2,3]
- 大神思路1:
1.找出重复的数字: 计算所有数字的和, 减去 set(输入的数组), 即可找到重复的数字.
2.找出丢失的数字: 计算1到n的 累加和, 减去 set(输入的数组)
Runtime: 230 ms, faster than 85.57% of Python3 online submissions for Set Mismatch.
Memory Usage: 15.9 MB, less than 23.96% of Python3 online submissions for Set Mismatch.
- 大神思路2:
1.找出重复的数字: 用Counter计数, 用 most_common 得出最常出现的.
2.找出丢失的数字: 计算1到n的 累加和, 减去 set(输入的数组)
Runtime: 203 ms, faster than 94.35% of Python3 online submissions for Set Mismatch.
Memory Usage: 15.9 MB, less than 23.96% of Python3 online submissions for Set Mismatch.
- 思路:
每两个进行对比, 若相同, 则返回.注意,要求是1-n, 若输入[2,2], 需要返回[1,2]
注意: 丢失的数字可能是 x+1 也可能是 1. 1 的情况为: 开头的数字不为1 且最后一个数字.
注意: 这数组没有排序, 重复的数字可能不是相邻的.
    '''
    def findErrorNums(self, nums: List[int]) -> List[int]:
        return [
            sum(nums) - sum(set(nums)), # 找出重复数字
            int(len( nums ) * ( len( nums ) + 1 ) / 2  - sum(set(nums)))
        ]
        # 思路2
        from collections import Counter
        c = Counter(nums)
        n = len(nums)
        res = []
        dup = c.most_common(1)[0][0]
        res.append(dup)        
        miss = n*(n+1) // 2 - (sum(nums) - dup)
        res.append(miss)
        return res
        
    '''
    # 219. Contains Duplicate II
    # https://leetcode.com/problems/contains-duplicate-ii/
    问题: 输入一组数字和k, 判断是否存在两个相同的数字, 且他们的距离小于等于k. (即在特定小范围内, 判断是否有重复的数字.)
    思路: 用一个字典存储每个数字的索引, 若发现存在相同数字, 对比他们的间距是否小于k, 小于则返回这两个索引, 若大于, 则更新数字的索引.
    Runtime: 1503 ms, faster than 34.08% of Python3 online submissions for Contains Duplicate II.
    Memory Usage: 27.2 MB, less than 53.63% of Python3 online submissions for Contains Duplicate II.
    '''
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # faster
        d = {} #d[num] is the last index for which i is seen
        for i, num in enumerate(nums):
            if i - d.get(num, -k-1) <= k:
                return True
            else:
                d[num] = i
        return False

        # save the num's pos
        map_num_pos     =   {}
        for i in range(nums.__len__()):
            if map_num_pos.get(nums[i]) is None:
                map_num_pos[nums[i]]    =   i
                continue
            diff    =   i   -   map_num_pos[nums[i]]
            if diff <= k:
                return True
            map_num_pos[nums[i]]    =   i

        return False
        
    '''
    # 12. Integer to Roman
    # https://leetcode.com/problems/integer-to-roman/
    问题: 输入一个数字, 转化为罗马数字. 罗马数字的一些规则:
    (1:I, 5:V, X:10, L:50, C:100, D:500, M:1000). 遇到相近的数字时,需要通过减法来表示. 比如4: IV, 9:IX, 40:XL, 400:CD, 900:CM.
    疑问: 49? 怎么表示 : XXXXVIIII, XLIX. 遇到特殊的就用特殊的组合表示.
    思路1:  对个位/十位/百位/千位分别声明一个解析函数.
    从最低位开始生成每一位对应的数字, 调用函数解析, 最后拼接得到目标.
    Runtime: 66 ms, faster than 79.63% of Python3 online submissions for Integer to Roman.
    Memory Usage: 13.9 MB, less than 80.12% of Python3 online submissions for Integer to Roman.
    '''
    def intToRoman(self, num: int) -> str:
        def parse_1(i):
            i   =   int(i)
            if i == 0:
                return ''
            elif i == 4:
                return 'IV'
            elif i == 9:
                return 'IX'
            elif i == 5:
                return 'V'
            elif i < 4:
                return 'I' * i
            else:
                return 'V' + 'I' * int(i-5)
            
        def parse_10(i):
            i   =   int(i)
            if i == 0:
                return ''
            elif i == 4:
                # 40 = 50 - 10
                return 'XL'
            elif i == 9:
                # 90 = 100 - 10
                return 'XC'
            elif i < 4:
                return 'X' * i
            else:
                return 'L' + 'X' * int(i-5)
            
        def parse_100(i):
            i   =   int(i)
            if i == 0:
                return ''
            elif i == 4:
                # 400 = 500 - 100
                return 'CD'
            elif i == 9:
                # 900 = 1000 - 100
                return 'CM'
            elif i < 4:
                return 'C' * i
            else:
                return 'D' + 'C' * int(i-5)
        
        def parse_1000(i):
            i   =   int(i)
            if i == 0:
                return ''
            else:
                return 'M' * i
        
        funs        =   [parse_1,parse_10,parse_100,parse_1000]
        parts       =   []
        while num > 0:
            if funs.__len__() == 1:
                parts.append( funs[0](num))
                break
            else:
                fun =   funs.pop(0)
                parts.append( fun(num%10))
                num     /=  10
            # print(parts)
        
        parts.reverse()
        return "".join(parts)
        '''
        method 2
        '''
        map = {1:'I', 5:'V', 10: 'X', 50:'L', 100:'C', 500:'D', 1000:'M', 4:"IV", 9:"IX", 40:"XL", 90:"XC", 400:"CD", 900:"CM", 2:"II", 3:"III"}
        num2chk = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4]
        
        stack = []
        def d2r(num):
            if num == 0:
                return
            if num in map:
                stack.append(map[num])
                return
            for val in num2chk:
                if num >= val:
                    stack.append(map[val])
                    d2r(num-val)
                    break
        d2r(num)
        return "".join(stack)
    
    '''
    # 692. Top K Frequent Words
    # https://leetcode.com/problems/top-k-frequent-words/
    问题: 输入一组单词和数字k, 返回k个最常出现的单词, 若频率一样,则按字母顺序排序.
    返回的列表按照出现频率和单词字母顺序排序.
    思路1: 用字典统计单词出现的频率, 按照频率排序他们.
    Runtime: 118 ms, faster than 43.88% of Python3 online submissions for Top K Frequent Words.
    Memory Usage: 14.1 MB, less than 27.71% of Python3 online submissions for Top K Frequent Words.
    '''
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # 思路2 : 
        freq=Counter(words)
        sortedDict=sorted(freq.items(),key=lambda x:(-x[1],x[0]))
        out=[key for key,val in sortedDict[:k]]
        return out
        
        # 思路1 : 
        # word_map        =   {}
        # ret             =   {}  # {3: ('asd','zxc')}
        # # 统计频率
        # for word in words:
        #     if word_map.get(word) is None:
        #         word_map[word]  =   1
        #         continue
        #     word_map[word]  +=  1
        
        # # 出现频率一样的放在同一个字典
        # for word,count in word_map.items():
        #     if ret.get(count) is None:
        #         ret[count]      =   []
        #         ret[count].append(word)
        #     else:
        #         ret[count].append(word)
        
        # # 根据出现次数排序
        # desc_words  =   sorted(ret.items(), key=lambda x:x[0], reverse=True)
        # r_li        =   []
        # for count, words in desc_words:
        #     # print(sorted(words))
        #     r_li.extend(sorted(words))
        
        # return r_li[:k]


        # # 用 word_map 的 value 进行降序排序 
        # desc_words  =   sorted(word_map.items(), key=lambda x:x[1], reverse=True)
        # print(word_map)

        # for word,count in desc_words:
        #     if ret.get(count) is None:
        #         ret[count]      =   []
        #         ret[count].append(word)
        #     else:
        #         ret[count].append(word)
        #     # if count <= k:
        #     #     ret.append(word)
        
        
        # return  sorted(ret)
    
    '''
    # 16. 3Sum Closest
    # https://leetcode.com/problems/3sum-closest/
    问题: 输入一个包含n个数的数组和目标target, 找出3个数的和与target最相近, 返回这个和
    思路: 这是一个组合问题. 相差最近可以用 最小绝对值的差 来寻找. 因此问题变成如何
    组合出3个数. 
    他人思路2:  先排序数组, 若最小的3个的和大于 target, 则直接返回他们; 若最大的3个和
    都小于target, 则直接返回. 
    通过遍历数组, 在内部通过双向搜索, 
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # 排序
        nums = sorted(nums)
        # 若最小的3个的和大于 target, 则直接返回他们;
        cur = sum(nums[:3])
        
        if cur > target:
            return cur
        
        # 若最大的3个和都小于target, 则直接返回. 
        cur = sum(nums[-3:])
        if cur < target:
            return cur
        
        res = sum(nums[:3])
        diff = 0x1ffffff
        for ind in range(len(nums)):
            left, right = ind + 1, len(nums) - 1
            while left < right:
                cur = nums[ind] + nums[left] + nums[right]
                
                if cur < target:
                    # 找最大的
                    left += 1
                elif cur > target:
                    # 找小一些的
                    right -= 1
                else:
                    return cur
            if abs(cur - target) < abs(diff):
                diff = cur - target
                res = cur
        return res
        
    '''
    # 1. Two Sum
    # https://leetcode.com/problems/two-sum/
    问题: 输入一组数字 和 target, 找出数组中两个数字,他们的和是target. 不能重复使用. 返回他们的索引. (是否可以小于 O(n^2) 的时间复杂度)
    注意: 元素可能重复, 但是不能重复用同一个元素. 每组输入仅有一个结果.
    思路1:
    用 target 减 每个元素, 判断 差 是否在数组中. 这种时间复杂度就是 O(N^2)
    Runtime: 2165 ms, faster than 28.62% of Python3 online submissions for Two Sum.
    Memory Usage: 14.9 MB, less than 95.40% of Python3 online submissions for Two Sum.

    思路2:
    空间换时间. 保存每个数字的索引.

    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Runtime: 152 ms, faster than 37.61% of Python3 online submissions for Two Sum.
        Memory Usage: 15.3 MB, less than 24.22% of Python3 online submissions for Two Sum.
        '''
        num_map     =   {}
        for i in range(len(nums)):
            sub_    =   target - nums[i]
            if num_map.get(sub_) is not None: # 注意遇到0索引的情况
                return [i, num_map.get(sub_)]
            else:
                num_map[nums[i]]    =   i
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            sub_    =   target - nums[i]
            tmp     =   nums[i]
            nums[i] =   0xffffffff      # 防止找到自身
            if sub_ in nums:
                i2  =   nums.index(sub_)
                return [i, i2]
            else:
                nums[i]=    tmp         # 修复



