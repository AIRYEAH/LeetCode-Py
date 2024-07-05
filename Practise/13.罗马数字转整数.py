#
# @lc app=leetcode.cn id=13 lang=python3
#
# [13] 罗马数字转整数
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        table = {
            "I": 1,
            "IV": 4,
            "V": 5,
            "IX": 9,
            "X": 10,
            "XL": 40,
            "L": 50,
            "XC": 90,
            "C": 100,
            "CD": 400,
            "D": 500,
            "CM": 900,
            "M": 1000,
        }

        i = 0
        num = 0
        while (i < len(s)):
            if (i+1 < len(s) and s[i]+s[i+1] in table):
                num += table[s[i]+s[i+1]]
                i += 1
            else:
                num += table[s[i]]

            i += 1

        return num


# @lc code=end
a = Solution()
b = a.romanToInt("IV")
print(b)
