#
# @lc app=leetcode.cn id=49 lang=python3
#
# [49] 字母异位词分组
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        # 思路
        # 1.遍历所有元素
        # 2.元素字符标准化排列后添加至哈希表
        # 3.每一次遍历的元素标准化后与哈希表中的Key比对，存在则加入元素，不存在则新建键值
        table = {}
        for i in strs:
            sortedKey = sorted(i)
            sortedKey = "".join(sortedKey)
            if (sortedKey in table):
                table[sortedKey].append(i)
            else:
                table[sortedKey] = []
                table[sortedKey].append(i)

        # print(table)
        return list(table.values())


# @lc code=end
a = Solution()
b = a.groupAnagrams(["a"])
# print(b)
