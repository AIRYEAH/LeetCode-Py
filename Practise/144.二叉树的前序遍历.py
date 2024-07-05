#
# @lc app=leetcode.cn id=144 lang=python3
#
# [144] 二叉树的前序遍历
#

# @lc code=start
# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        # 递归，深度优先遍历
        def dfs(root: TreeNode):
            if root is None:
                return

            # 前序根左右
            res_f.append(root.val)
            dfs(root.left)
            dfs(root.right)

            # 中序左根右
            # dfs(root.left)
            # res_m.append(root.val)
            # dfs(root.right)

            # 后序左右根
            # dfs(root.left)
            # dfs(root.right)
            # res_b.append(root.val)

        res_f = []
        # res_m = []
        # res_b = []
        dfs(root)
        # print(res_f)
        # print(res_m)
        # print(res_b)
        return res_f

        # @lc code=end


# 构造树
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

a = Solution()
b = a.preorderTraversal(root)
