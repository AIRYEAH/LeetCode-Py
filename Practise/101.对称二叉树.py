#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
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
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def recur(L: TreeNode, R: TreeNode):
            # 左右结点不存在，说明为叶子结点，只要值相等就满足对称性
            if not L and not R:
                return True

            # 左右结点的值不相等，不满足对称性
            if L.val != R.val:
                return False

            return recur(L.left, R.right) and recur(L.right, R.left)
        return True
        # def recur(L, R):
        #     if not L and not R:
        #         return True
        #     if not L or not R or L.val != R.val:
        #         return False
        #     return recur(L.left, R.right) and recur(L.right, R.left)

        # return not root or recur(root.left, root.right)

        # def printNodeVal():


# @lc code=end


a = Solution()
root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)
b = a.isSymmetric(root)
print(root)
