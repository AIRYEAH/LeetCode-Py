#
# @lc app=leetcode.cn id=28 lang=python3
#
# [28] 找出字符串中第一个匹配项的下标
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # 暴力解
        table = {}
        len1 = len(haystack)
        len2 = len(needle)
        i = 0
        while (i < len1):
            # 匹配上第一个字符时，开始向后逐一匹配，全部匹配上即可返回下标
            if (haystack[i] == needle[0]):
                for index1, index2 in zip(range(i, len1), range(0, len2)):
                    if (haystack[index1] != needle[index2]):
                        break

                    if (index2 == len2-1):
                        return i

            i += 1

        return -1

        # @lc code=end


a = Solution()
b = a.strStr("asdasfdasfasfasf", "sf")
print(b)
