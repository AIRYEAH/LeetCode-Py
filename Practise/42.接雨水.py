#
# @lc app=leetcode.cn id=42 lang=python3
#
# [42] 接水
#

# @lc code=start
class Solution:
    def trap(self, height: list[int]) -> int:
        # length = len(height)
        # l = 0
        # r = 1
        # v = 0
        # fd = []
        # while (r < length):
        #     fd.append(height[r]-height[l])
        #     l += 1
        #     r += 1

        # # print(height)
        # # print(length)
        # # print(fd)
        # # print(len(fd))
        # # while (l < r and r < length):
        # #     if (height[r] > 0 and height[l] > 0):
        # #         v += min(height[r], height[l])*(l-r)-height[r:l]
        # #         l = r
        # #     r += 1

        # 难以理解的鬼方法,一坨屎
        # res = 0
        # lenth = len(height)
        # l = 0  # 左指针
        # r = lenth-1  # 右指针
        # f_max = 0  # 从左向右遍历过程中遇到的柱子最大值
        # b_max = 0  # 从右往左遍历过程中遇到的柱子最大值
        # while (l < r):
        #     f_max = max(f_max, height[l])
        #     b_max = max(b_max, height[r])
        #     if f_max < b_max:
        #         res += f_max-height[l]
        #         l += 1
        #     else:
        #         res += b_max-height[r]
        #         r -= 1

        res = 0
        length = len(height)
        l = 0
        r = length-1
        l_max = []  # 当柱子高度单调递增时，左边的缺口能存储的最大水量
        r_max = []  # 当柱子高度单调递减时，右边的缺口能存储的最大水量
        pre_max = 0
        res = 0

        while (l < length):
            pre_max = max(pre_max, height[l])
            l_max.append(pre_max)
            l += 1

        pre_max = 0
        while (r > 0):
            pre_max = max(pre_max, height[r])
            r_max.append(pre_max)
            r -= 1
        r_max.reverse()

        for i, j, k in zip(l_max, r_max, height):
            res += max(min(i, j)-k, 0)  # 储水量必大于0

        return res

        # @lc code=end
a = Solution()
b = a.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
print(b)
