#
# @lc app=leetcode.cn id=20 lang=python3
#
# [20] 有效的括号
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # 输入长度非偶数
        if (len(s) % 2 != 0):
            return False

        # 字典表
        dic = {"(": ")", "[": "]", "{": "}"}
        # print(dic["("])

        # 检测堆栈
        check = []
        for i in s:
            # 栈空则压入字符再指向下一步
            if (check == []):
                check.append(i)
                continue

            # 检查当前压入元素是否与上一个元素匹配，匹配则出栈栈顶元素，不匹配则继续压入字符
            if (check[-1] in dic):
                if (dic[check[-1]] == i):
                    check.pop()
                else:
                    check.append(i)
            else:
                check.append(i)

        # 栈空说明输入符合条件
        if (check == []):
            return True

        return False
# @lc code=end


a = Solution()
r = a.isValid("({}[])")
print(r)
# dic = [")", "("]
# dic.pop()
# print(dic)
