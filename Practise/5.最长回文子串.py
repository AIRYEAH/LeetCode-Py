#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 两边向中间对比
        # res = ""
        # s_len = len(s)
        # if (s_len <= 1):
        #     return s

        # l = 0
        # r = s_len-1
        # j = s_len
        # for i in range(0, s_len):
        #     l = i
        #     r = s_len-1
        #     while (r > l):
        #         if (s[l] != s[r]):
        #             j = r
        #             r -= 1
        #             continue

        #         if (s[l] == s[r]):
        #             r -= 1
        #             l += 1

        #         if (r <= l):
        #             currentStr = s[i:j]
        #             if (len(currentStr) > len(res)):
        #                 res = currentStr

        # # 查找不到最长回文字符串，仅返回单个字符
        # if (res == ""):
        #     return s[0]

        # 中间向两边对比
        res = ""
        s_len = len(s)
        if (s_len <= 1):
            return s

        l = 0
        r = 0
        j = 0
        for i in range(1, s_len):
            currentStr = ""

            # 偶数串
            l = i
            r = i
            while (l > 0 and r < s_len):
                r += 1
                if (s[l] == s[r]):
                    l -= 1
                    r += 1

                if (s[l] != s[r]):
                    currentStr = s[l:r]
                    if (len(currentStr) > len(res)):
                        res = currentStr

            # 奇数串
            l = i
            r = i
            while (l > 0 and r < s_len):
                if (s[l] == s[r]):
                    l -= 1
                    r += 1
                    continue

                if (s[l] != s[r]):
                    currentStr = s[l:r]
                    if (len(currentStr) > len(res)):
                        res = currentStr

        # 查找不到最长回文字符串，仅返回单个字符
        if (res == ""):
            return s[0]

        return res
        # @lc code=end


a = Solution()
b = a.longestPalindrome("aba")
print(b)
