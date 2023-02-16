'''
二叉树相关算法.
'''
from typing import Optional, List
import heapq
import queue
from collections import *
# Definition for a binary tree node.
null,Null    =   None,None    # 对 null 进行转义
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def list_2_tree(values:list):
    '''
    把 list 数据转为一颗二叉树. 输入的list是按层级遍历的结果.
    '''
    if not values:
        return  None
    root                =   TreeNode(values.pop(0))
    last_level_nodes    =   [root]  # 保存前一层的节点(从左往右)
    while values.__len__() > 0:
        new_level_nodes =   []  # 保存下一层需要遍历的节点
        
        while last_level_nodes.__len__() > 0:
            cur_node    =   last_level_nodes.pop(0)
            if values.__len__() > 0:
                left_val    =   values.pop(0)
                if left_val is not None:
                    cur_node.left   =   TreeNode(left_val)
                    new_level_nodes.append(cur_node.left)
            
            if values.__len__() > 0:
                right_val    =   values.pop(0)
                if right_val is not None:
                    cur_node.right   =   TreeNode(right_val)
                    new_level_nodes.append(cur_node.right)
        
        # 需要遍历的下一层节点
        last_level_nodes    =   new_level_nodes
    
    return root



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
- https://leetcode.com/problems/maximum-depth-of-binary-tree/description/
- 104. Maximum Depth of Binary Tree (Easy)
- 问题:  
求树的最大深度
- 思路:
递归即可
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    '''
- https://leetcode.com/problems/path-sum-iii/   
- 437. Path Sum III
- 问题:  
输入一棵二叉树, 找出所有子路径上节点的和 为 targetSum 的路径个数.
路径只能是上下结构, 不用拐外.
- tag: 前缀和
- 他人思路:
一个字典存储当前走过的所有路径的和, 用 cur_sum - targetSum 得出需要的前缀路径 pre_sum ,
从字典获取 pre_sum 的个数, 即可得到由当前节点构成的子路径和为targetSum的个数.
------> pre_sum
--------------> cur_sum
*******-------> targetSum
Beats 98.65%
    '''
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        res_count       =   0
        path_sums       =   defaultdict(int)
        
        def dfs_prefix_path_sum(node:Optional[TreeNode], cur_sum):
            nonlocal res_count, path_sums
            if node:
                cur_sum     +=  node.val
                # 当前路径构成的 和 等于 target 则结果+1, 因为初始 cur_sum 没有根节点
                if cur_sum == targetSum:
                    res_count   +=  1
                # 计算需要的前缀和是多少
                pre_sum     =   cur_sum -   targetSum
                # 获取能够组成目标前缀和的路径数量
                res_count   +=  path_sums.get(pre_sum, 0)
                
                # 路径数量+1
                path_sums[cur_sum]  +=  1
                dfs_prefix_path_sum(node.left, cur_sum)
                dfs_prefix_path_sum(node.right, cur_sum)
                # 递归返回, 移除当前节点, 路径数量-1
                path_sums[cur_sum]  -=  1
        
        dfs_prefix_path_sum(root, 0)
        return res_count


    '''
- https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
- 1519. Number of Nodes in the Sub-Tree With the Same Label (medium)
- 问题:  
输入一个没有方向的树， 包含 n 个 节点. 0 是根节点, 每个节点有一个 label 用 labels 数组表示. edges 数组表示节点之间有一条边.
返回 ans 数组, 每一项表示 node-i 的所有子树中 和 node-i 有相同 label 的节点个数, 包括 node-i 自身.
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], labels = "abaedcd"
Output: [2,1,1,1,1,1,1]
- 思路:
遍历所有节点, 给每个节点找出他们的子树节点列表, 遍历子树节点列表统计相同 label节点个数.
    '''
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        ans     =   [0] * n
        
        def get_sub_tree_nodes(node_i):
            '''
            获取输入节点构成的子树 的 节点列表, 返回节点的id
            :param      node_i      节点id值
            :returns    []      子树的节点id列表
            '''
            ret         =   []
            begin_nodes =   [node_i]
            while begin_nodes.__len__() > 0:
                begin   =   begin_nodes.pop()
                for edge in edges:
                    if edge[0] == begin:
                        ret.append(edge[1])
                        begin_nodes.append(edge[1])
            return ret

        for i in range(n):
            ans[i] +=   1       # 至少一个相同的节点, 即自身
            nodes   =   get_sub_tree_nodes(i)
            for node_id in nodes:
                if labels[node_id] == labels[i]:
                    ans[i] +=   1
        
        return ans
        
    '''
- https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
- 1443. Minimum Time to Collect All Apples in a Tree(medium)
- 问题:  
有n个节点的无向树, 其中一些节点包含苹果, 返回从0节点出发并返回到0节点, 最小需要的步数能够摘所有苹果. 其中 edge[i] = [ai,bi] 表示有一条 ai 到 bi的边. hasApple[i] = true 表示 i节点有苹果. ie: 7个节点, 边由 edges 表示, 苹果所在节点由 hasApple数组表示
Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], hasApple = [false,false,true,false,true,true,false]
Output: 8 
- 思路:
replace with your idea.
    '''

    '''
- https://leetcode.com/problems/binary-tree-preorder-traversal/
- 144. Binary Tree Preorder Traversal(easy)
- 问题:  
二叉树的前序遍历
- 思路1:
递归Beats 69.37%
- 思路2
队列 Beats 95.77%
    '''
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack       =   [root]
        node_vals   =   []
        while stack.__len__() > 0:
            node    =   stack.pop()
            if node:
                node_vals.append(node.val)
                stack.append(node.right)
                stack.append(node.left)
        return  node_vals

        # node_vals   =   []
        # def preorder(node:Optional[TreeNode]):
        #     if node:
        #         node_vals.append(node.val)
        #         preorder(node.left)
        #         preorder(node.right)
        # preorder(root)
        # return  node_vals


    '''
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/description/
    # 124. Binary Tree Maximum Path Sum (hard)
- 问题: 
输入一颗二叉树, 每两个相邻的节点构成一个 path , 问最大的 path 的和是多少.
- 思路:
后序遍历, 找出左子树的最大 path 和 右子树的最大 path. 然后对比三个值:
左子树最大 path, 右子树最大 path, 加上当前节点的最大path
    '''
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_val    =   root.val
        def post_order(node):
            if node:
                left    =   post_order(node.left)
                right   =   post_order(node.right)
                canditates  =   [node.val]
                if left is not None and left > 0:
                    canditates.append(left)
                    canditates.append(left + node.val)
                if right is not None and right > 0:
                    canditates.append(right)
                    canditates.append(right+node.val)
                if left is not None and right is not None:
                    canditates.append(left+right+node.val)
                return max(canditates)
            else:
                return None
        
        return post_order(root)

    '''
    # https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
    # 1026. Maximum Difference Between Node and Ancestor (medium)
- 问题: 
输入一颗二叉树, 找出节点的差的绝对值的最大值. 理解错了, 是任意的子节点
节点的距离不超过深度2. 即 a 节点最多只能到达它的孙节点.
(节点的值都是正数)
- 思路1 爆破:
从根节点往下, 对比节点的所有父节点
- 思路2 最值:
从根节点往下到任意节点, 保存遇到的最大值和最小值, 计算当前节点与父节点中的两个最值对比即可.
Beats 61.22%
- 思路3 链路最值:
从根节点往下遍历, 更新链路上的最值, 当遇到叶节点时, 返回链路上最值的差
Beats 93.13%
    '''

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def root_2_leaf(node, max_val, min_val):
            if node:
                max_val =   max(node.val, max_val)
                min_val =   min(node.val, min_val)
                return max(
                    root_2_leaf(node.left, max_val, min_val),
                    root_2_leaf(node.right, max_val, min_val)
                )
            else:
                return abs(max_val-min_val)

            
        return root_2_leaf(root, root.val, root.val)

        self.max_diff   =   0
        def find_max_diff(node, max_val, min_val):
            '''
            递归, max_val 是到当前节点的最大值, min_val 是到当前节点的最小值
            '''
            if node:
                self.max_diff   =   max(self.max_diff, 
                    abs(node.val - max_val), 
                    abs(node.val - min_val))
                max_val =   max(node.val, max_val)
                min_val =   min(node.val, min_val)
                find_max_diff(node.left, max_val, min_val)
                find_max_diff(node.right, max_val, min_val)
        
        find_max_diff(root,root.val, root.val)
        return self.max_diff
        
    
    '''
    # https://leetcode.com/problems/leaf-similar-trees/
    # 872. Leaf-Similar Trees (easy)
- 问题: 
输入两个二叉树, 判断他们的所有叶子节点是否值都相同.
- 思路1:  
深度遍历即可.
Beats 52.92%
    '''
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def get_leafs(node:TreeNode, leafs:list):
            if not node:
                return
            if not node.left and not node.right:
                leafs.append(node.val)
            get_leafs(node.left, leafs)
            get_leafs(node.right, leafs)
            
        leafs1 = []
        get_leafs(root1, leafs1)
        leafs2 = []
        get_leafs(root2, leafs2)
        return leafs1 == leafs2
    '''
    # https://leetcode.com/problems/range-sum-of-bst/
    # 938. Range Sum of BST (easy)
- 问题: 
输入一个二叉树根节点, 返回在 [low,high] 区间数字的和
- 思路1:  
深度遍历即可.
    Runtime: 27 ms, faster than 98.21% of Python3 online submissions for Same Tree.
    Memory Usage: 13.8 MB, less than 75.48% of Python3 online submissions for Same Tree.
    '''
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sum_    =   0
        if not root:
            return 0
        sum_    =   self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        if root.val >= low and root.val <=high:
            return root.val + sum_
        else:
            return sum_
    '''
    # https://leetcode.com/problems/same-tree/
    # 100. Same Tree (easy)
    问题: 判断两个二叉树是否相同
    思路1:  判断指针是否存在, 判断值是否存在. 递归判断子节点.
    Runtime: 27 ms, faster than 98.21% of Python3 online submissions for Same Tree.
    Memory Usage: 13.8 MB, less than 75.48% of Python3 online submissions for Same Tree.
    '''
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return  True
        if not p or not q:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

    '''
    # https://leetcode.com/problems/binary-tree-inorder-traversal/
    # 94. Binary Tree Inorder Traversal (easy)
    问题: 输入二叉树根节点, 返回中序遍历.
    思路1: 中序遍历: 左/根/右
    Runtime: 58 ms, faster than 38.98% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 13.9 MB, less than 59.37% of Python3 online submissions for Binary Tree Inorder Traversal.
    思路2:
    Runtime: 62 ms, faster than 24.70% of Python3 online submissions for Binary Tree Inorder Traversal.
    Memory Usage: 13.9 MB, less than 59.37% of Python3 online submissions for Binary Tree Inorder Traversal.
    '''
    def inorderInsert(self, node: Optional[TreeNode], ret:list):
        if node:
            self.inorderInsert(node.left, ret)
            ret.append(node.val)
            self.inorderInsert(node.right, ret)
    def inorderTraversal(self, root: Optional[TreeNode], ret=None) -> List[int]:
        # 思路1
        # vals        =   []
        # self.inorderInsert(root, vals)
        # return  vals
        # 思路2
        if not root:
            return
        if ret is None:
            cur     =   []
            self.inorderTraversal(root.left, cur)
            cur.append(root.val)
            self.inorderTraversal(root.right, cur)
            
            return cur
        else:
            self.inorderTraversal(root.left, ret)
            ret.append(root.val)
            self.inorderTraversal(root.right, ret)

