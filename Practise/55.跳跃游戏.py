#
# @lc app=leetcode.cn id=55 lang=python3
#
# [55] 跳跃游戏
#

# @lc code=start
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxlen = 0
        orilen = len(nums)

        # 只有一个元素的情况
        if (orilen == 1):
            return True

        # 最后一步不用检查
        for i in range(0, orilen-1):
            o = nums[i]+i

            # 更新最远到达距离
            if (o > maxlen):
                maxlen = o

            # 最远到达的地方等于当前下标，且当前对应值为0
            if (maxlen == i and nums[i] == 0):
                return False

            # print(maxlen)
            # 下标加下标对应的步长若大于等于数组总长，则能到达最后一个下标
            if (maxlen >= orilen-1):
                return True

        return False
# @lc code=end


a = Solution()
b = a.canJump([0, 2, 3, 0])
print(b)
