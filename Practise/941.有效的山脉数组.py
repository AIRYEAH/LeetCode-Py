#
# @lc app=leetcode.cn id=941 lang=python3
#
# [941] 有效的山脉数组
#

# @lc code=start
class Solution:
    def validMountainArray(self, arr: list[int]) -> bool:
        maxNum = max(arr)
        prviousNum = arr[0]
        arrLen = len(arr)
        isIncrese = True

        # 长度限制
        if (arrLen < 3):
            return False

        # 首末数若为数组最大值，直接返回False
        if (arr[0] == maxNum or arr[-1] == maxNum):
            return False

        # 遍历
        for i in range(1, len(arr)):
            # 不连续增长或衰减
            if (prviousNum == arr[i]):
                return False

            if (isIncrese):
                if (prviousNum >= arr[i]):
                    return False
                prviousNum = arr[i]
            else:
                if (prviousNum <= arr[i]):
                    return False
                prviousNum = arr[i]

            if (arr[i] == maxNum):
                isIncrese = False

        return True

# @lc code=end


a = Solution()
b = a.validMountainArray([3, 5, 5])
print(b)
