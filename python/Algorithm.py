'''
未分类的算法
'''
from collections import Counter
import collections
from typing import List


def guess(self, x):
    pass
class Solution:
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
        r       =   ''
        for c in sorted(
            Counter(s).items(),
            key= lambda x: -x[1]
            ):
            r += c[0] * c[1]
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



