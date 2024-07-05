#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        isPositive = True if x > 0 else False
        x_str = str(abs(x))
        # print(x_str[::-1])
        x_str = x_str[::-1]
        res = int(x_str)
        if (isPositive == False):
            res = res*-1

        if (res > (2**31)-1 or res < -(2 ** 31)):
            return 0

        return res
# @lc code=end


a = Solution()
b = a.reverse(-12312)
print(b)
