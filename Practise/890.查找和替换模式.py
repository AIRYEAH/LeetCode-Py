#
# @lc app=leetcode.cn id=890 lang=python3
#
# [890] 查找和替换模式
#

# @lc code=start
class Solution:
    def findAndReplacePattern(self, words: list[str], pattern: str) -> list[str]:
        table = {}
        result = []
        for word in words:
            table.clear()
            # 长度不匹配，跳过
            if (len(word) != len(pattern)):
                continue

            isMatch = True
            # 双迭代器
            for chr, pchr in zip(word, pattern):
                # 每次模式匹配都需要重新构造映射表
                if (chr not in table):
                    table[chr] = pchr
                if (chr in table and table[chr] != pchr):
                    isMatch = False

            if (isMatch == False):
                continue

            # 检查映射表的键值对应值是否存在重复，当存在多个键对应同一值时，说明字符串模式不匹配
            # prviousValue = None
            # for i in table:
            #     if prviousValue == None:
            #         prviousValue = table[i]
            #         continue

            #     # 存在多键值对应同一值得情况，中断循环，模式不匹配
            #     if table[i] == prviousValue:
            #         isMatch = False
            #          break

            #     prviousValue = table[i]

            # 通过比较键值与键值对应值的长度来判断是否存在多个键对应同一值的情况
            value = []
            for i in table:
                if table[i] not in value:
                    value.append(table[i])

            if (len(value) != len(table)):
                isMatch = False

            if (isMatch):
                result.append(word)

        return result
# @lc code=end


a = Solution()
b = a.findAndReplacePattern(["badc", "abab", "dddd", "dede", "yyxx"], "baba")
print(b)

# word = {"a": 1}
# word["b"] = 2
# print(word)

# b = [1, 2, 3]
# c = [4, 5, 6]
# d = [6, 7, 8, 9]
# # 多重迭代器
# for x, y, z in zip(b, c, d):
#     print(x+y+z)

# b = {"a": 1, "b": 2, "c": 3}
# for i in b:
#     print(b[i])

# print(len(b))
