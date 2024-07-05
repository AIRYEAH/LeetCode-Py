#
# @lc app=leetcode.cn id=434 lang=python3
#
# [434] 字符串中的单词数
#

# @lc code=start
class Solution:
    def countSegments(self, s: str) -> int:
        res = s.split()
        return len(res)
        # @lc code=end


a = Solution()
b = a.countSegments("Hello, my name is John. Damn")
print(b)
