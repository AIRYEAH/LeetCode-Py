#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 穷举法,超时
        # length = len(height)
        # maxVolume = 0
        # for i in range(0, length):
        #     for j in range(i+1, length):
        #         maxVolume = max(maxVolume, (j-i)*min(height[i], height[j]))

        # return maxVolume

        # 双指针
        left = 0  # 左边界
        right = len(height)-1  # 右边界
        res = 0
        currentS = 0
        while (left < right):
            # 计算当前面积S=两端较小的高度值*两边下标差值
            currentS = min(height[right], height[left])*(right-left)
            res = max(currentS, res)
            # 关键，两边向中间逼近
            if (height[left] < height[right]):
                # 左高小于右高，向中间逼近，寻找新高度
                left += 1
            else:
                # 右高小于左高，向中间逼近，寻找新高度
                right -= 1

        return res
        # @lc code=end


a = Solution()
b = a.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(b)
