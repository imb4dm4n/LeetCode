'''
图算法
'''
from typing import List

class Solution:
    '''
- replace with url
- replace with problem title (easy)
- 问题:  
replace with problem description
- 思路:
replace with your idea.
    '''
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
