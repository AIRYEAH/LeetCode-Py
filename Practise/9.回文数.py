#
# @lc app=leetcode.cn id=9 lang=python3
#
# [9] 回文数
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = str(x)
        b = str(x)[::-1]
        if (a == b):
            return True
        return False
# @lc code=end
