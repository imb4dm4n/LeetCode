'''
动态规划问题
'''
from collections import Counter
import collections
from typing import List
from functools import lru_cache
import heapq
import math
import bisect
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
- https://leetcode.com/problems/minimum-falling-path-sum/
- 931. Minimum Falling Path Sum (Medium)
输入 nxn 矩阵, 返回最小的坠落和.
Input: matrix = [
[2,1,3],
[6,5,4],
[7,8,9]]
Output: 13 = 8 + 4 + 1
- 思路: dp 类似机器人寻路到右下角, 找出最小的路径, 这里不同的是可以从顶层任意开始到最后一层任意节点
base case 就一层, 返回当前层最小的那个
状态: 处于不同层的特定节点;
转移: 向下一层移动 (x+1,y), (x+1,y+1), (x+1,y-1).
核心: 从第一层开始遍历, 尝试所有的可能直到最后一行, 得出一个最小值, 同时记录经过的每个节点最小值
用一个2d数组交替保存每个可能的起始节点, 到每一层的对应节点的最小值. 
因为是 nxn 正方形矩阵, 因此左上角一定可以到达右下角, 存在大量的重复计算. 
每个cell保存它到最后一行的最小距离.
dp函数定义: 计算并返回 从当前起始坐标 (x,y) 到最后一行的最小距离和
[14,1,3]  [x,13]   
[13,12]   [13,12,12]
[7,8,9]   [7,8,9]
Beats 19.30% ...
- 大神思路
直接每一行往下计算, 每个单元格可能的最小值, 最后求个 min 就可以.. Beats 46.14%
    '''
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # 大神
        n   =   len(matrix)
        for i in range(1, n):
            for j in range(0, n):
                matrix[i][j]    +=   min(
                    matrix[i-1][max(0, j-1)], # the smart way
                    matrix[i-1][min(n-1, j+1)],
                    matrix[i-1][j],
                )
        return min(matrix[n-1])

        # DP 方法 Beats 19.30% ...
        n   =   len(matrix)
        UNREACHABLE =   10001 # 限制cell的数值是 -100 ~ 100, n <= 100 , 因此路径和 < 10000
        dp  =   [[UNREACHABLE] * n for i in range(n)]
        dp[n-1] =   matrix[n-1]

        def dp_calc_min_path_sum(x, y):
            '''
            计算并返回 从当前起始坐标 (x,y) 到最后一行的最小距离和
            '''
            if x >= n or y >= n or y < 0:
                return UNREACHABLE
            if x == n-1: # 最后一行直接返回
                return matrix[x][y]
            if dp[x][y] != UNREACHABLE:
                return dp[x][y]
            
            path_sums   =   [
                dp_calc_min_path_sum(x+1, y) + matrix[x][y],
                dp_calc_min_path_sum(x+1, y+1) + matrix[x][y],
                dp_calc_min_path_sum(x+1, y-1) + matrix[x][y],
                UNREACHABLE
            ]
            dp[x][y]    =   min(path_sums)
            return dp[x][y]
        
        res     =   UNREACHABLE
        for j in range(n):
            dp_calc_min_path_sum(0, j)
            res     =   min(res, dp[0][j])
        return res


    '''
- https://leetcode.com/problems/coin-change/
- 322. Coin Change (Medium)
- 问题:  
输入 coins 数组表示不同面值, 一个整数 amount 表示想要的金额,返回最少需要的 coin 个数, 若凑不到返回 -1
- 思路1: dp - top down
amount 根据 coin 的变化而变化, 进一步修改 硬币个数.
base case: amount = 0, 返回0
状态: 当前要凑的金额 cur_amount
转移: 不同的硬币选择 i , 修改状态到 cur_amount- coins[i]
dp 函数定义: 输入一个金额 x 返回最小能够凑到的 amount 使用的 coin 个数
Beats 37.51%
- 思路2: dp - bottom up
遍历 cur 从0-amount, 对应最优的硬币个数为 1 + min(choice[cur - coins_i])
    '''
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        lease_coins =   [amount+1] * (amount) # 如果有面值1 那么 amount+1 将超过可能的硬币数量最大值
        lease_coins[0]=0
        for cur in range(amount):
            for val in coins:
                if cur - val < 0:
                    continue
                if lease_coins[cur-val] != amount +1:
                    lease_coins[cur] = min(lease_coins[cur], 
                                    1+ lease_coins[cur-val])
        print(lease_coins)
        return lease_coins[amount-2] if lease_coins[amount-2] != amount+1 else -1
        

        if not amount:
            return  0
        
        INF     =   -66666
        INF2    =   10000000
        amount_coin =   [INF] * (amount + 1)  # 存储一个 amount 最少需要的硬币个数
        def dp_change(cur_amount):
            if cur_amount < 0:
                return -1
            if cur_amount == 0:
                return 0
            # 查询备忘录
            if amount_coin[cur_amount] != INF:
                return amount_coin[cur_amount]
            
            res     =   INF2
            for val in coins:
                sub_res =   dp_change(cur_amount - val)
                if sub_res == -1: # 子问题无解则跳过
                    continue
                res = min(res,  sub_res + 1) # 否则加上当前1个硬币
            amount_coin[cur_amount] = res if res != INF2 else -1
            return amount_coin[cur_amount]
        
        dp_change(amount)
        return amount_coin[amount]

    '''
- https://leetcode.com/problems/reducing-dishes/
- 1402. Reducing Dishes (Hard)
- 问题:  
厨师准备食材和炒菜, 输入 n 道菜的满意度, 每道菜需要一个单元的时间去完成.
一道菜的时间满意度为 (炒菜+准备)耗时 * 菜的满意度time[i] * satisfaction[i].
返回最大的 时间满意度总和, 厨师可以丢弃一些菜单并任意修改顺序.
Input: satisfaction = [-1,-8,0,5,-9]
Output: 14
Explanation: After Removing the second and last dish, the maximum total like-time coefficient will be equal to (-1*1 + 0*2 + 5*3 = 14).
- 思路:
大神思路: 为了让分值最大,那么只要这道菜累积到目前的贡献值是 > 0 的就做它, 否则不做.
累加前缀和可以对同一个值 + n 次, 使得第一道菜在最后的时候是正确的索引
    '''
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        n = len(satisfaction)
        presum, res = 0, 0
        for i in range(n):
            presum += satisfaction[i]
            if presum < 0:
                break
            res += presum
        return res
    

        satisfaction.sort()
        n   =  len(satisfaction) +1
        dp  =  [[0]*n for i in range(n)]

        def dp_max_satisfaction(offset, cook_seq):
            if offset >= len(satisfaction) or cook_seq >= len(satisfaction):
                return 0
            # print("off {} seq {} n {}".format(offset, cook_seq, n))
            if dp[offset][cook_seq-1]:
                print("found dp result")
                return dp[offset][cook_seq-1]
            dp[offset][cook_seq-1] = max(
                dp_max_satisfaction(offset+1, cook_seq+1) + satisfaction[offset] * cook_seq,
                dp_max_satisfaction(offset+1, cook_seq),
            )
            return dp[offset][cook_seq-1]
        
        dp_max_satisfaction(0, 1)
        print(dp)
        return dp[0][0]


        # dp  =   [0] * n
        final_max_satisfaction  =   0   # 最终的最大值
        # print(satisfaction)

        def dp_max_satif(cook_id, cook_time, cur_satisfaction):
            '''
            动态的炒当前的菜:
            :param      cook_id     第几道菜 相对于 satisfaction 数组cook_time
            '''
            nonlocal final_max_satisfaction
            if cook_id >= n:
                final_max_satisfaction  =   max(
                    final_max_satisfaction,
                    cur_satisfaction
                )
                return 0
            
            # print("[+]cook_id is {} dp cook = {}".format(cook_id, dp[cook_id]))
            # if dp[cook_id]:
            #     return dp[cook_id]
            
            def max_satif(dish_id, is_cook, cook_time1, cur_satif):
                '''
                动态的炒当前的菜:
                :param      dish_id     第几道菜 相对于 satisfaction 数组
                :param      is_cook     是否炒这道菜
                :param      cook_time   真正炒菜的顺序, 某一道菜不被炒则传递相同cook_time
                '''
                # print("dish id {} is_cook {} ct {}".format(dish_id, is_cook, cook_time1))
                if is_cook:
                    t=  dp_max_satif(dish_id+1, cook_time1 + 1, satisfaction[dish_id] * cook_time1 + cur_satif)
                    # print("t=", t)
                    # return t
                else:
                    a= dp_max_satif(dish_id+1, cook_time1, cur_satif)
                    # print("a=",a)
                    # return a
            # time_satif= [
            max_satif(cook_id, True, cook_time  ,cur_satisfaction),
            max_satif(cook_id, False, cook_time ,cur_satisfaction)
            # ]
            # print("id {} max satif {}".format(cook_id, time_satif))
            # dp[cook_id] =   max(time_satif)
            # return dp[cook_id]
            # time_satif  =   [
            #         max_satif(cook_id, True, cook_time, ca) ,
            #         max_satif(cook_id, False, cook_time, ca)  ,
            #         # max_satif(cook_id+1, True, cook_time+1) + satisfaction[cook_id],
            #         # max_satif(cook_id+1, False, cook_time+1)  + satisfaction[cook_id]
            #     ]
            # print("cook id {} satis {}".format(cook_id, time_satif))
            # dp[cook_id] =   max(time_satif)
            # return dp[cook_id]
        
        dp_max_satif(0, 1, 0)
        # print(dp)
        return final_max_satisfaction
        return dp_max_satif(0, 1, 0)

    '''
- https://leetcode.com/problems/minimum-cost-for-tickets/
- 983. Minimum Cost For Tickets (Medium) dp
- 问题:  
提前准备一年的旅行, days[] 数组表示要旅游的是[1,365] 的哪一天, costs[a,b,c] 分别表示旅游1天、7天、30天需要的钱。 问最少完成一年旅行的钱是多少？
Input: days = [1,4,6,7,8,20], costs = [2,7,15]
Output: 11
Explanation: For example, here is one way to buy passes that lets you travel your travel plan:
On day 1, you bought a 1-day pass for costs[0] = $2, which covered day 1.
On day 3, you bought a 7-day pass for costs[1] = $7, which covered days 3, 4, ..., 9.
On day 20, you bought a 1-day pass for costs[0] = $2, which covered day 20.
In total, you spent $11 and covered all the days of your travel.

- dp思路: 核心是遍历所有可能的方案, 找出最省钱的方案; 计算方案时存在重复计算, 因此可以用 dp 数组保存结果.
Beats 83.55%
状态是当前处于哪一天旅游或者说是目前消费总额; 选择是选择哪种旅游方式(1,7,30),不同选择进入新的状态;
dp 函数： 第i天可以选择3种旅游方式, 对应下一次做选择时, 天数会有3种情况i+1,i+6,i+29;
进一步递归计算. 但是每一天的选择计算到最终时，需要保存结果，然后求最小值。
每一天的cost状态是动态计算的,对于某一天的选择，会有一个cost值，同时会影响后面n天的cost为0或者xx；
计算到最后一天时，加入结果，或者直接对比取最小值；

- 大神 Beats 87.21%
存储从0到每一天的累积开销, 若今天不旅游, 则用前一天作为今天的开销;
若今天要旅游, 则寻找3种方案中最省钱的方案
    1.今天旅游1天, 则总开销为 今天的 + 昨天累积的
    2.今天旅游7天票, 则总开销为 今天的 + 7天前累积的开销
    3.今天旅游30天票, 则总开销为 今天的 + 30天前累积的开销
    '''
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # Beats 83.55%
        if not days:
            return 0
        
        n   =   len(days)
        dp  =   [0] * n     # 保存旅游日最优的花钱
        
        def dp_min_cost(begin):
            if begin >= n:
                return 0
            
            if dp[begin]:   # 直接返回计算过的最优值
                return dp[begin]
            
            def mincost(day_index, travel_type):
                '''
                特定一天选择的旅游类型, 并对其余的 旅游日期, 做出不同操作. 因为有的票可以 cover 一些旅游日，因此需要跳过计算
                '''
                if day_index >= n:
                    return 0
                if travel_type == 0:
                    return costs[travel_type] + dp_min_cost(day_index+1)
                elif travel_type == 1:
                    cover_days =   days[day_index] + 7      # 问题: 不能+6 必须 + 7
                    x=bisect.bisect_left(days[day_index:], cover_days)
                    return costs[travel_type] + dp_min_cost(begin+x)    # 问题: 要begin+x 而不是 x
                else:
                    cover_days =   days[day_index] + 30      # 问题: 不能+29 必须 + 30
                    x=bisect.bisect_left(days[day_index:], cover_days)
                    print("[2]cur_day= {} coverTo= {} insert at ={}".format(days[day_index], cover_days, x))
                    return costs[travel_type] + dp_min_cost(begin+x)
            
            # 对于特定一天有3种选择, 全部都计算, 取最小值写入 dp 
            possible_costs  =   [
                mincost(begin, 0),
                mincost(begin, 1),
                mincost(begin, 2),
            ]
            dp[begin]   =   min(possible_costs)
            return dp[begin]
        return  dp_min_cost(0)

        # 大神思路 初始化第0天为0累积开销
        daily_cost  =   {0:0}
        for d in days:
            daily_cost[d]   =   0
        for i in range(1, 366):
            if daily_cost.get(i) is None:
                daily_cost[i] = daily_cost[i-1]
            else:
                daily_cost[i]      =   min(
                    daily_cost[i-1] + costs[0],
                    daily_cost[max(0,i-7)] + costs[1],
                    daily_cost[max(0,i-30)] + costs[2],
                )
        return daily_cost[365]
    
    '''
- https://leetcode.com/problems/minimum-path-sum/
- 64. Minimum Path Sum (Medium) dp 
- 问题:  
输入 mxn 矩阵，每一个包含数字，从左上角到右下角最小的路径和是多少？
- tag:  
- 思路:
动态规划？ 和机器人寻路一样？ 从右下角往左上角搜索，选择小的节点。
状态是什么? 选择是什么?
状态是到当前坐标 (i,j) 的 pathSum; 选择是向右还是向下移动; (反过来想, 当前左边是从哪个节点过来的)
用一个二维数组保存到每一个坐标(i,j)的最优 pathSum, 那么到 (i,j)的最优路径就是
dp[i][j]= min(dp[i-1,j] + grid[i,j], 
              dp[i][j-1]) + grid[i,j] );

优化dp空间, 实际只需要一维数组即可? 因为第一行的值是固定的, 用前缀和转list即可;
第二行每一个坐标对应的 dp[j] 是否更新呢? 若 grid[i][j] < dp[j] 则更新 
dp[j] = min( dp[j]+grid[i][j] , grid[i-1][j]+grid[i][j]), j > 0;
计算完毕后, 返回 dp 数组最后一个数字即可。
Beats 30.96%
- 他人思路
对原始数组修改, 先做行的累加, 再做列的累加, 最后再更新 grid [i][j] Beats 94.31%
    '''
    def minPathSum(self, grid: List[List[int]]) -> int:
        # 修改原始数组
        m = len(grid)
        n = len(grid[0])
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]  # 先做行的累加
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]  # 再做列的累加
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1]) # 再更新 grid [i][j]
        return grid[-1][-1]

        # 自己的 dp 计算比较慢 ...
        dp  =   list(itertools.accumulate(grid[0]))
        rows    =   len(grid)
        columns  =   len(grid[0])

        if rows == 1:       # 只有一行则直接返回最后一个结果
            return dp[-1]
        
        for i in range(1, rows):
            for j in range(0, columns):
                if j == 0:
                    dp[j]   =   dp[j]   +   grid[i][j]  # 第0个需要累加原始的
                else:
                    dp[j]   =   min(
                        dp[j-1] +    grid[i][j] ,# 左边一个
                        dp[j]   +   grid[i][j]   # 上边一个
                    )
        
        return dp[-1]
        
    '''
- https://leetcode.com/problems/number-of-zero-filled-subarrays/
- 2348. Number of Zero-Filled Subarrays (Medium)
- 问题:  
输入数组 返回都是0的子数组个数.
Input: nums = [1,3,0,0,2,0,0,4]
Output: 6
- 思路:
状态: 当前子数组的0个数; 选择: 若当前数字是0, 可以选择加入当前数字或不加入. 若不加入, 则更新当前状态数组 []

用一个数组 count_0_from_pos 存储每个索引开始的包含0的子数组个数. 然后统计所有索引开始0的个数
当前索引i开始0的个数为 
    1.若当前索引的数字不是0, 则 count_0_from_pos[i] = 0
    2.若当前索引数字是0, 则 count_0_from_pos[i] = count_0_from_pos[i+1] + 1
    Beats 5.9% ..... 不过算法竟然是对的 ... 
- 他人思路1 Beats 78.26% .. 嗯 确实是累加的思路, 统计有多少个0, 和那个 numPathSum 类似, 前缀和
    '''
    def zeroFilledSubarray(self, nums: List[int]) -> int: 
        # 他人思路1
        total_zero_subarrays = current_zero_subarrays = 0
                
        for num in nums:
            if num == 0:
                current_zero_subarrays += 1
                total_zero_subarrays += current_zero_subarrays
            else:
                current_zero_subarrays = 0
                
        return total_zero_subarrays
    
        n   =   len(nums)
        count_0_from_pos    =   [0] * (n+1)
        i   =   n
        
        while i > 0:
            if nums[i-1] == 0:
                count_0_from_pos[i-1]   =   count_0_from_pos[i] + 1
            else:
                count_0_from_pos[i-1]   =   0
            i -= 1
        
        return sum(count_0_from_pos)

    '''
- https://leetcode.com/problems/can-place-flowers/
- 605. Can Place Flowers (Easy)
- 问题:  
输入一个坑位数组, 0表示空着，1表示种了花，输入一个数字n表示还要种的个数，种花必须保持一个坑位间隔，判断能否种n个花。
Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
- 大神思路
count - number of flowers we can plant
prev - what was on the previous plot
prev | cur
...1 | 0 => can't plant => prev = 0
...0 | 1 => can't plant => prev = 1
...0 | 0 => can plant!! => count++; prev = 1
...1 | 1 => violation!!! => count--; prev = 1

- 思路:
状态：当前索引 offset 坑位是否种花，若遇到已经中了花，则移动到下一个坑位。
    当前坑位能否种花的前提是: prev=0, next=0,cur=0
选择： 种花或者不种
一个flag表示当前坑位能否种花，如果能种花则 计数器 n - 1，
从0遍历坑位长度，直到结尾或者n=0退出循环。
返回 n 是否等于0
    '''
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count, prev = 0, 0

        for cur in flowerbed:
            if cur == 1:
                if prev == 1: # violation!
                    count -= 1
                prev = 1
            else:
                if prev == 1: # can't plant
                    prev = 0 
                else:
                    count += 1
                    prev = 1 # the cur plot gets taken
            
        return count >= n
        count   =   len(flowerbed)
        def plant_flower(offset, res_to_plant):
            '''
            在当前 offset 种花, 返回最后还有几个花要种
            '''
            if offset >= count or res_to_plant == 0:
                return res_to_plant

            if offset == count-1:
                return res_to_plant - 1

            if offset == 0 and \
                offset + 1 < count and \
                flowerbed[offset] == 0 and\
                flowerbed[offset+1] == 0:
                # flowerbed[offset]   =   1
                return plant_flower(offset+2, res_to_plant-1)
            
            if flowerbed[offset] == 0 and \
                offset + 1 < count and flowerbed[offset+1] == 0:
                # flowerbed[offset]   =   1
                return plant_flower(offset+2, res_to_plant-1)
            # 边界情况

            return plant_flower(offset+2,res_to_plant)
        
        return plant_flower(0, n)==0

        # can_plant   =   False
        count_bed   =   len(flowerbed)
        i           =   0
        prev_plant  =   -1
        while i < count_bed:
            if n == 0:
                break
            print("pre plant ={} i = {}".format(prev_plant, i))
            if prev_plant > -1 and i - prev_plant== 1:
                
                i   +=  1
                continue
            # 当前坑位可以种花
            if i + 1 < count_bed and \
                flowerbed[i]==0 and \
                flowerbed[i+1]==0 :
                prev_plant  =   i
                
                print("11pre plant ", prev_plant)
                n   -=  1 
                i +=    2
                continue
            elif i == count_bed-1 and flowerbed[i]==0:
                n   -=  1

            prev_plant=i
            i +=    1

        return n == 0
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
- https://leetcode.com/contest/weekly-contest-331/problems/house-robber-iv/
- 6346. House Robber IV
- 问题:  
抢劫一个街道上的房子, 每个房子有一定的现金, 劫匪只会从相邻的房子偷，小偷的能力
是所有可以偷的选项的最大值， 返回小偷的所有选项中的，最小能力。k 表示小偷最多偷的房子数量
- 思路
先获取当前数字的 max, 然后递归往下 把 k -1, 并移除 max,
最后把他们合并起来, 求 min ?
用一个最小堆保存 小偷的最小实力, 然后 dp 递归下去, 加入到这个最小堆

    '''
    def minCapability(self, nums: List[int], k: int) -> int:
        small_capability    =   []

        def dp_find_max(idx, cur_max, x, rob_cur):
            '''
            :param      x   还要抢几个
            '''
            nonlocal nums
            
            
            if x == 0 and cur_max != -1 and rob_cur:
                # print("[@] x==0 add max {}".format(cur_max))
                heapq.heappush(small_capability, cur_max)
                return
            
            if idx >= len(nums):
                # print("reach end  max {} x {} rob {}".format(cur_max,x,rob_cur))
                return
            
            # print("num {} max= {} x= {} rob {}".format(nums[idx], cur_max,x,rob_cur))
            # 抢这一间
            if rob_cur:
                cur_max =   max(nums[idx], cur_max)
                # print("加入第一个 cur_max={}".format(cur_max))
                dp_find_max(idx+2, cur_max, x-1, True) 
                dp_find_max(idx+2, cur_max, x-1, False) 
            # 不抢这个 则抢下一个
            else:
                dp_find_max(idx+1, cur_max, x, True)
                dp_find_max(idx+1, cur_max, x, False)

            # 加入当前第一个
            
        dp_find_max(0, -1, k, True)
        dp_find_max(0, -1, k, False)
        if small_capability[0] == -1:
            heapq.heappop(small_capability)
        # print("heap {}".format(small_capability))
        return small_capability[0]

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
