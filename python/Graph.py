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
- https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/    
- 2316. Count Unreachable Pairs of Nodes in an Undirected Graph (Medium)
- 问题:  
输入包含n个节点的无向图, 返回两两不连接的接点对个数.
- tag: Graph
- 思路:
对于一个节点而言， 有两个属性:
    1.可以到达的节点个数 2.不可到达的节点个数
对于可到达的节点而言，对应的每个节点都是可以互相到达，而他们也共享不可到达的节点个数。
因此对输入的图按照是否可互相到达 进行聚类，然后统计类的个数。
[4,1,2] => 4 x (1+2) + 1 x 2 = 14
    '''
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        group_counter   =   []  # 每一个表示互相可到达的节点个数
        

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

    '''
- https://leetcode.com/problems/find-if-path-exists-in-graph/
- 1971. Find if Path Exists in Graph (easy)
- 问题:  
输入包含 n 个节点的图, 每个节点用一个数字表示. 一个数组表示节点之间的边:
[(1,2), (2,3)] 表示 1->2  2->3 . 问是否存在 x->y的路径, 存在返回 true
- 思路:
从输入中找到 source 的输出列表, 加入待搜索路径, pop 一个节点, 判断目标是不是 dst,
若是, 则返回 true, 若不是, 则再次写入搜索路径列表, 遍历直到搜索路径列表为空
    '''
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True
        paths_to_search =   []
        for i, edge in enumerate(edges):
            if edge[0] == source:
                paths_to_search.append(edge)
                if paths_to_search.__len__() == 2:
                    break
        
        while paths_to_search.__len__() > 0:
            edge1    =   paths_to_search.pop()
            if edge1[1] ==  destination:
                return True
            for i, edge in enumerate(edges):
                if edge[0] == edge1[1]:
                    paths_to_search.append(edge)
        
        return False
