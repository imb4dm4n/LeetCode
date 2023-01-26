'''
图相关算法
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
- tag: Graph
- 思路:
replace with your idea.
    '''
    '''
- https://leetcode.com/problems/find-the-town-judge/
- 997. Find the Town Judge (easy)
- 问题:  
一个镇上有n个人, 其中可能有个人是法官. 若有法官, 则存在以下约束: 1.法官不信任任何人; 2. 任何人都信任法官. 只有一个法官,  输入一个trust数组, trust[i]=[ai,bi]表示a信任b. 找出这个法官的下标, 若不存在返回 -1
- tag: Graph
- 思路:
.... 一个人可以信任多个人, 同时也信任法官 ... 相当于是顶级节点
是一个图的问题, 多个节点指向一个节点, 一个节点不指向任何节点.
用一个map就可以解决, ai->ci, bi->ci, di->ci, 并且不存在 ci 作为 key 的map, 那么说明ci就是法官的下标. 
每个人, 信任他的人的个数.
Beats36.39%
边界处理: 可能需要统计下人数是否为 n
    '''
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) <= 1 and n == 1:
            return 1
        map_trust   =   defaultdict(set)
        for person, been_trust in trust:
            # if not map_trust.get(been_trust):
            #     map_trust[been_trust]   =   set()
            
            map_trust[been_trust].add(person)
            
        for been_trust, persons in map_trust.items():
            if len(persons) == n-1:
                for persons in map_trust.values():
                    if been_trust in persons:
                        return -1
                return been_trust

        return -1
        judges  =   set(map_trust.values())
        # there are more than one person can be trust
        if len(judges) > 1:
            return -1

        print(map_trust)
        judges  =   list(judges)
        # a judge can not trust anyone
        if map_trust.get(judges[0]) is not None:
            return -1

        if len(map_trust.keys()) != n-1:
            return -1
        
        return judges[0]
