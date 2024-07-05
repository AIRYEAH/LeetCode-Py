#
# @lc app=leetcode.cn id=438 lang=python3
#
# [438] 找到字符串中所有字母异位词
#

# @lc code=start
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        # p_set = set(p)
        # p_len = len(p)
        # index = 0
        # length = len(s)
        # res = []
        # cache_set = set([])
        # while (index < length):
        #     if (s[index] not in p_set):
        #         cache_set.clear()
        #         index += 1
        #         continue

        #     if (s[index] in p_set):
        #         cache_set.add(s[index])
        #         index += 1

        #     if (cache_set == p_set):
        #         res.append(index-p_len)

        # 双指针与字符串标准化
        s_len = len(s)
        p_len = len(p)
        res = []
        if (s_len < p_len):
            return res

        l = 0
        r = p_len
        standard = sorted(p)
        while (r <= s_len):
            if (sorted(s[l:r]) == standard):
                res.append(l)

            l += 1
            r += 1

        return res
        # @lc code=end


a = Solution()
b = a.findAnagrams("bbba", "ab")
print(b)
