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

from LinkedList import ListNode

class TryNode:
    def __init__(self ) -> None:
        self.is_end =   False
        self.children   =   {}

'''
- https://leetcode.com/problems/implement-trie-prefix-tree/
- 208. Implement Trie (Prefix Tree) Medium
- 问题
Tries 树的实现
- 思路

'''
# Beats 94.34%
class Trie(object):
    
	def __init__(self):
		self.trie = {}


	def insert(self, word):
		t = self.trie
		for c in word:
			if c not in t: t[c] = {}
			t = t[c]
		t["-"] = True


	def search(self, word):
		t = self.trie
		for c in word:
			if c not in t: return False
			t = t[c]
		return "-" in t

	def startsWith(self, prefix):
		t = self.trie
		for c in prefix:
			if c not in t: return False
			t = t[c]
		return True

# Beats 85.87%
# class Trie:
#     def __init__(self):
#         self.children = defaultdict(Trie)
#         self.isWord = False

#     def insert(self, word: str) -> None:
#         cur = self
#         for c in word:
#             cur = cur.children[c]
#         cur.isWord = True

#     def search(self, word: str) -> bool:
#         cur = self
#         for c in word:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         return cur.isWord

#     def startsWith(self, prefix: str) -> bool:
#         cur = self
#         for c in prefix:
#             if c not in cur.children:
#                 return False
#             cur = cur.children[c]
#         return True
    
# class Trie:
# beat 51 
#     def __init__(self):
#         self.root   =   TryNode()



#     def insert(self, word: str) -> None:
#         '''
#         void insert(String word) Inserts the string word into the trie.
#         '''
#         node    =   self.root
#         for c in word:
#             # 字符不存在则创建 try-node
#             if not node.children.get(c):
#                 node.children[c]    =   TryNode()
#             node    =   node.children[c]
#         node.is_end =   True
        

#     def search(self, word: str) -> bool:
#         '''
#         Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
#         '''
#         node    =   self.root
#         for c in word:
#             if not node.children.get(c):
#                 return False
#             node    =   node.children[c]
        
#         return node.is_end 
        

#     def startsWith(self, prefix: str) -> bool:
#         ''' 
#         Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
#         '''
#         node    =   self.root
#         for c in prefix:
#             if not node.children.get(c):
#                 return False
#             node    =   node.children[c]
        
#         return True 
'''
- https://leetcode.com/problems/design-browser-history/
- 1472. Design Browser History (Medium)
- 问题:  
设计浏览器的前进、后退、浏览功能的历史记录器。 
- 思路1: 二叉树/ 双向链表
root 表示根节点
cur 表示当前浏览的页面
二叉树的 left 表示后退， right 表示前进， visit 表示在 cur 节点插入新节点并把之前cur后面的节点都清除掉
Beats 28.32%
- 思路2: 双栈
一个保存历史 history , 一个 future 保存 backward 时pop出 history 的数据,
forward 时从 future pop数据
Beats 16.87%  ...
- 思路3: list 计数
Beats 95.27%
'''
class BrowserHistory:

    def __init__(self, homepage: str):
        self.history    =   [homepage]
        self.pos        =   0

    def visit(self, url: str) -> None:
        '''
        插入新的节点并移动指针
        '''
        self.pos    +=  1
        self.history    =   self.history[:self.pos]
        self.history.append(url)
        # print("history ", self.history)

    def back(self, steps: int) -> str:
        # 要么移动到第一个 要么就是 pos - steps
        self.pos    =   max(0, self.pos -   steps)
        
        return self.history[self.pos]
        

    def forward(self, steps: int) -> str:
        # 要么移动当前 + steps 要么移动到最后一个
        self.pos    =   min(self.history.__len__()-1, 
                            self.pos+steps)
        
        return self.history[self.pos]
    

    # def __init__(self, homepage: str):
    #     self.history    =   [homepage]
    #     self.future     =   []

    # def visit(self, url: str) -> None:
    #     '''
    #     插入新的节点并移动指针
    #     '''
    #     self.history.append(url)
    #     self.future =   []

    # def back(self, steps: int) -> str:
    #     while self.history.__len__() > 1 and steps > 0:
    #         steps   -=  1
    #         self.future.append(self.history.pop())
        
    #     return self.history[-1]
        

    # def forward(self, steps: int) -> str:
    #     while steps > 0 and self.future.__len__() > 0:
    #         self.history.append(self.future.pop())
    #         steps   -=  1
        
    #     return self.history[-1]
    

    def __init__(self, homepage: str):
        self.root   =   TreeNode(homepage)
        self.cur    =   self.root

    def visit(self, url: str) -> None:
        '''
        插入新的节点并移动指针
        '''
        node    =   TreeNode(url)
        self.cur.right  =   node
        node.left       =   self.cur
        self.cur        =   node
        

    def back(self, steps: int) -> str:
        while self.cur and self.cur.left and steps > 0:
            self.cur    =   self.cur.left
            steps       -=  1
        return self.cur.val
        

    def forward(self, steps: int) -> str:
        while self.cur and self.cur.right and steps > 0:
            self.cur    =   self.cur.right
            steps       -=  1
        return self.cur.val


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
- https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
- 1161. Maximum Level Sum of a Binary Tree (Medium)
- 问题:  
输入二叉树, 寻找最小的层数x使得对应层所有节点的和最大
- 思路:
层序遍历, 必须遍历所有的才知道最大的 sum.
记录对应的层级 和 max_sum 
    '''
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        each_level  =   [0]
        def dfs(node, level):
            nonlocal each_level

            if node:
                each_level[level-1] += node.val
                if len(each_level) <= level and (node.left or node.right) :
                    # print("{} add level {} nodeval {}" .format(level,len(each_level), node.val))
                    each_level.append(0)
                dfs(node.left, level+1)
                dfs(node.right, level+1)
        dfs(root, 1)
        s=list(enumerate(each_level,1))
        
        print(sorted(s, key=lambda x:(-x[1],x[0])))
        return sorted(s, key=lambda x:(-x[1],x[0]))[0][0]


        max_level   =   1
        cur_level   =   1
        max_sum = -1000000
        tmp_queue   =   [root]
        while len(tmp_queue) > 0:
            n   =   len(tmp_queue)
            cur_sum =   0
            
            for i in range(n):
                node    =   tmp_queue.pop(0)
                cur_sum += node.val
                if node.left:
                    tmp_queue.append(node.left)
                if node.right:
                    tmp_queue.append(node.right)
            
            print("cur sum {} cur level {} max sum {}".format(
                cur_sum,cur_level, max_sum
            ))
            if cur_sum > max_sum:
                max_sum =   cur_sum
                max_level = cur_level
            cur_level += 1
        
        return max_level


    '''
- https://leetcode.com/problems/maximum-width-of-binary-tree/
- 662. Maximum Width of Binary Tree (Medium)
- 问题:  
输入二叉树, 找出最宽的那一层的宽度. 宽度由最左边非空节点到最右非空节点构成的宽度(其中null节点也被计算, 但是最右边后面的 null 不算)
- 思路:
BFS遍历每一层, 遇到空节点时, 往下一层加入两个空节点, 如果当前层是 [a,b,nul,nul,nul] 则宽度为2, 若当前层是 [a,nul,nul,nul] 宽度为0, 若当前层是 [a,nul,nul,b,nul]则宽度为4
    '''
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res     =   0
        if not root:
            return res
        bfs =   [root]
        max_width   =   0
        while bfs:
            level_len   =   len(bfs)
            # print(level_len)
            # need to calculate current level width
            left,right   =   0, level_len - 1
            while left < right:
                if bfs[left] == None:
                    left    +=  1
                if bfs[right] == None:
                    right    -=  1
                if bfs[left] and bfs[right]:
                    break
            if left > right:
                break
            max_width   =   max(max_width, right - left + 1)
            # print("max width ", max_width)

            while level_len > 0:
                node    =   bfs.pop(0)
                if node:
                    bfs.append(node.left)
                    bfs.append(node.right)
                else:
                    bfs.append(None)
                    bfs.append(None)
                level_len   -=  1
        return max_width


    '''
- https://leetcode.com/problems/longest-zigzag-path-in-a-binary-tree/
- 1372. Longest ZigZag Path in a Binary Tree (Medium)
- 问题:  
输入一个二叉树, 可以做以下操作
1.随意选择一个节点和方向
2.根据方向移动到下一个节点
3.与前一个方向相反选择另一个方向移动
4.一直移动直到无法再移动
返回经过节点数最多的路径. 起始节点不算经过的节点
- 思路:
对于一个节点来说, 选择左或者右, 其返回值是确定的. 每一个节点计算根据前一个选择得到的结果返回, 
以及与前一个选择相反 得到的, 与 max_len 对比.
前序 DFS 遍历, 返回当前节点构成最长的 节点数量
    '''
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        max_len     =   0
        left,right,unknown    =   0,1,2
        def dfs_zig_zag(node:TreeNode, direction:int):
            '''
            direction = True 表示当前层需要选择右节点
            '''
            if not node:
                return 0
            if direction == left:
                desire  =   1 + dfs_zig_zag(node.left, right)
            elif direction == right:
                desire  =   1 + dfs_zig_zag(node.right, left)
            else:
                the_other_way   =   0 + dfs_zig_zag(node.right, left)
            

    '''
- https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/
- 106. Construct Binary Tree from Inorder and Postorder Traversal (Medium)
- 问题:  
输入一棵二叉树的中序和后续遍历, 构造出这个二叉树
- 思路:
用后序遍历得到root节点, 去中序遍历拆分出左子树和右子树, 递归的生成节点
    '''
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inorder_map =   {}
        for i, n in enumerate(inorder):
            inorder_map[n]  =   i

        n, post_index   =   len(inorder)    ,   len(inorder)    -1
        def build_from_pivot(start, end, post_idx):
            if start > end:
                return None
            node    =   TreeNode(postorder[post_idx-1])
            inorder_idx     =   inorder_map[node.val]
            node.right  =   build_from_pivot(inorder_idx+1, end, post_idx -1)
            node.left  =   build_from_pivot(start , inorder_idx-1, post_idx -1)

        
        return build_from_pivot(0, post_index, post_index)

    '''
- https://leetcode.com/problems/check-completeness-of-a-binary-tree/
- 958. Check Completeness of a Binary Tree (Medium)
- 问题:  
输入一棵二叉树, 判断它是否完全, 即除了最后一层的叶节点可以没有完整的节点, 其他都是满的
- 大神思路:
如果是完全二叉树, 用 bfs 遍历, 得到的最后一层最后一个节点之后, 应该是空的, 若还有其他节点
则说明不是完全二叉树 Beats 86.18%
    '''
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        bfs     =   [root]
        i       =   0
        
        # 遇到第一个 None 节点会 break
        while bfs[i]:
            bfs.append(bfs[i].left)
            bfs.append(bfs[i].right)
            i   +=  1
        
        # 最后一层的 最后一个节点之后应该没有节点了, 否则不是完全二叉树
        return not any(bfs[i:])
    
    
    '''
- https://leetcode.com/problems/sum-root-to-leaf-numbers/
- 129. Sum Root to Leaf Numbers (Medium)
- 问题:  
每个节点表示一个数字, 求 每个根到叶节点组成的路径表示的数字的和.
- 思路:
dfs遍历, 若当前节点非空, 则把前一层结果*10并加上当前结果, 传递给下一层;
节点为空则添加到 总和.
    '''
    def sumNumbers(self, root: Optional[TreeNode], base=0) -> int:
        # 思路2 Beats 97.50%
        if not root:
            return 0
        if not root.left and not root.right:
            return base + root.val
        
        next_base   =   (base+root.val) * 10
        left_sums   =   self.sumNumbers(root.left, next_base)
        right_sums   =   self.sumNumbers(root.right, next_base)
        return left_sums + right_sums
        
        # 思路1 Beats 20.45%
        res     =   0
        def dfs_sum(node, cur_sum):
            nonlocal res
            if node:
                cur_sum *= 10
                cur_sum +=  node.val
                
                # 叶节点则添加结果, 不能继续递归 否则会计算两次结果
                if not node.left and not node.right:
                    res     +=  cur_sum
                # 非叶节点则继续遍历
                else:
                    dfs_sum(node.left, cur_sum)
                    dfs_sum(node.right, cur_sum)


        dfs_sum(root, 0)
        return res
    '''
- https://leetcode.com/problems/symmetric-tree/description/
- 101. Symmetric Tree (Easy)
- 问题:  
输入一棵二叉树 判断是否对称
- 思路:
对称的二叉树在根节点相同的情况下, 左子树等于右子树
    '''
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def symmetric(node_a, node_b):
            if not node_a and not node_b:
                return True
            if not node_a or not node_b:
                return False
            if node_b.val != node_a.val:
                return False
            return symmetric(node_a.left, node_b.right) and symmetric(node_a.right, node_b.left)
        return symmetric(root, root)
    '''
- https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
- 109. Convert Sorted List to Binary Search Tree (Medium)
- 问题:  
输入一个链表头, 转为平衡二叉搜索树
- 思路1:
转list 然后找到中间节点转换. 注意区间是 [left, mid-1]; [mid+1,right] Beats 37.72%
- 思路2:
快慢指针 Beats 29.36%
    '''
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow,fast = head, head.next
        while fast.next and fast.next.next:
            fast    =   fast.next.next
            slow    =   slow.next
        
        mid     =   slow.next
        slow.next   =   None
        node    =   TreeNode(mid.val)
        node.left   =   self.sortedListToBST(head)
        node.right  =   self.sortedListToBST(mid.next)
        return node

        # 方法1
        if not head:
            return None
        nodes = []
        while head:
            nodes.append(head.val)
            head    =   head.next
        
        def to_bst(list_nodes, left, right):
            if right < 0 or left > right:
                return None
            mid =   (left+right) // 2
            if mid < 0 or mid > len(nodes):
                return None
            cur_node    =   TreeNode(list_nodes[mid])  
            cur_node.left   =   to_bst(list_nodes, left, mid-1)
            cur_node.right   =   to_bst(list_nodes, mid+1, right)
            return cur_node
        
        return to_bst(nodes,0,len(nodes)-1)



    '''
- https://leetcode.com/problems/find-duplicate-subtrees/
- 652. Find Duplicate Subtrees (Medium)
- 问题:  
输入一颗二叉树, 返回所有拥有相同结构的子树.只需要返回他们的头节点列表即可
- 思路:
所有子树, 因此每个节点构成的子树都要对比.
前序遍历深度优先, 到底部的时候开始构造子树, 写入子树列表,
    '''
    '''
- https://leetcode.com/problems/minimum-distance-between-bst-nodes/
- 783. Minimum Distance Between BST Nodes (Easy)
- 问题:  
二叉搜索树上任意两节点的最小差值.... 没理解到位, 任意节点
- 思路:
二叉搜索左边小右边大, 因此搜索深度不能超过子节点, 其实就是中序遍历即可
Beats 81.58%
    '''
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        prev    =   None
        min_diff    =   0x1ffffff

        def inorder(node):
            nonlocal prev,min_diff 
            
            if node:
                inorder(node.left)
                if prev:
                    min_diff    =   min(min_diff, (abs(node.val - prev.val)))
                prev    =   node
                inorder(node.right)
        inorder(root)
        return min_diff

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

