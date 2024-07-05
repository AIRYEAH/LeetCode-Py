#
# @lc app=leetcode.cn id=145 lang=python3
#
# [145] 二叉树的后序遍历
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
    def postorderTraversal(self, root: Optional[TreeNode]) -> list[int]:
        def dfs(root: TreeNode):
            if root is None:
                return

            # 后序遍历，左右根
            dfs(root.left)
            dfs(root.right)
            res.append(root.val)

        res = []
        dfs(root)
        # print(res)
        return res
        # @lc code=end


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

a = Solution()
b = a.postorderTraversal(root)
