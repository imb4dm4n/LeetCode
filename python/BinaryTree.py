'''
二叉树相关算法.
'''
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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

