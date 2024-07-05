#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows < 2:
            return s

        # 定义行字符串，用于最后每行字符串的拼接
        res = ["" for row in range(numRows)]
        i = 0
        isMoveDown = True
        for c in s:
            res[i] += c

            if (isMoveDown):
                i += 1
            else:
                i -= 1

            if i == 0 or i == numRows-1:
                isMoveDown = not isMoveDown

        return "".join(res)

        # 操你妈傻逼leetcode测试用例
        # 单行输入直接返回
        # if (numRows == 1):
        #     return s

        # table = {}
        # isMoveDown = True  # 填充趋势
        # row = 0
        # coloum = 0
        # res = ""
        # for c in s:
        #     table[int(str(row)+str(coloum))] = c
        #     if (isMoveDown):
        #         row += 1
        #     else:
        #         row -= 1
        #         coloum += 1

        #     if (row >= numRows-1 or row == 0):
        #         isMoveDown = not isMoveDown

        # for i in sorted(table.keys()):
        #     res += table[i]
        # return res

        # @lc code=end


a = Solution()
b = a.convert("ABCD", 2)
print(b)
