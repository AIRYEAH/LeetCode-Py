#
# @lc app=leetcode.cn id=872 lang=python3
#
# [872] 叶子相似的树
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
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # 深度优先搜索
        # 注:区别yield与yield from，前者相当于return，返回一个不可迭代对象；后者相当于返回一个可迭代对象
        def dfs(node: TreeNode):
            if not node.left and not node.right:
                yield node.val  # 没有左右节点，说明是末端节点，返回末端节点值
            else:
                if node.left:
                    yield from dfs(node.left)  # 向左递归遍历
                if node.right:
                    yield from dfs(node.right)  # 向右递归遍历

        seq1 = list(dfs(root1)) if root1 else list()
        seq2 = list(dfs(root2)) if root2 else list()
        print(seq1)
        print(seq2)

        return seq1 == seq2

# @lc code=end


# a = Solution()
# a.leafSimilar([3, 5, 1, 6, 2, 9, 8, None, None, 7, 4],
#               [3, 5, 1, 6, 7, 4, 2, None, None, None, None, None, None, 9, 8])
