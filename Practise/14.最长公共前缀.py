#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        # 极致复杂的方法，面向测试用例编程
        if (strs == []):
            return ""

        if (len(strs) == 1):
            return strs[0]

        res = []
        index = 0
        for i in range(1, len(strs)):
            if (res == []):
                for c1, c2 in zip(strs[i-1], strs[i]):
                    if (c1 == c2):
                        res.append(c1)
                    else:
                        break

                # 第一轮比对就没有相同前缀，可直接返回
                if (res == []):
                    return ""
            else:
                # 长度限定
                if (len(strs[i]) < len(res)):
                    del res[len(strs[i]):]

                for c1, c2 in zip(res, strs[i]):
                    if (c1 == c2):
                        index += 1
                        continue
                    else:
                        del res[index:]
                        break

                if (res == []):
                    return ""
                index = 0

        return "".join(res)

        # @lc code=end


a = Solution()
b = a.longestCommonPrefix(["ca", "c", "bba", "bacb", "bcb"])
print(b)
