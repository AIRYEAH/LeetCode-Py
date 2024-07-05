#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子�?
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 傻逼题做的挫败感好强啊，去你妈的傻逼玩意儿算法
        # if (s == ""):
        #     return 0

        # if (len(s) == 1):
        #     return 1

        # currentStr = []
        # currentStrlen = 1
        # maxStrlen = 0
        # i = 0
        # j = 0
        # while (i < len(s) and j < len(s)):
        #     j += 1

        #     if (j > len(s)-1):
        #         if (currentStrlen > maxStrlen):
        #             maxStrlen = currentStrlen
        #         break

        #     # if (s[j] != s[i]):
        #     #     i += 1
        #     #     currentStrlen += 1
        #     #     continue
        #     if (s[j] not in s[i:j]):
        #         currentStr = s[i:j]
        #         currentStrlen += 1
        #         continue
        #     else:
        #         if (currentStrlen > maxStrlen):
        #             maxStrlen = currentStrlen
        #         i = j
        #         currentStrlen = 1

        # return maxStrlen
        # 哈希表记录所有不重复元素的最新坐标，通过坐标差值以及哈希表长度来反应元素非重复字符串的长度
        # dic, res, i = {}, 0, -1
        # for j in range(len(s)):
        #     if s[j] in dic:
        #         i = max(dic[s[j]], i)  # 更新左指针 i
        #     dic[s[j]] = j  # 哈希表记录
        #     res = max(res, j - i)  # 更新结果
        # return res

        # 再度实现，哈希表
        # dic = {}
        # i = -1
        # j = 0
        # maxlen = 0

        # while (j < len(s)):
        #     if (s[j] in dic):
        #         # 当存在重复字符时，更新左边界
        #         i = max(dic[s[j]], i)
        #     # 常规情况下，将新字符填入哈希表并记录下标
        #     dic[s[j]] = j
        #     # 非重复字符串长度为下标差值，每次比较只要和上一次记录的长度比较即可
        #     maxlen = max(maxlen, j-i)
        #     j += 1

        # 三刷，双指针哈希表
        dic = {}
        length = len(s)
        l = -1
        r = 0
        maxlen = 0
        while (r < length):
            if (s[r] in dic):
                l = max(dic[s[r]], l)

            dic[s[r]] = r
            maxlen = max(maxlen, r-l)
            r += 1

        return maxlen

        # @lc code=end


a = Solution()
b = a.lengthOfLongestSubstring("pwwkew")
print(b)
