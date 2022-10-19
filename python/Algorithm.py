'''
未分类的算法
'''
from collections import Counter
from typing import List




class Solution:
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



