#
# @lc app=leetcode.cn id=15 lang=python3
#
# [15] 三数之和
#

# @lc code=start
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        # 穷举，超时
        # length = len(nums)
        # res = []
        # for i in range(0, length-2):
        #     for j in range(i+1, length-1):
        #         for z in range(j+1, length):
        #             if (nums[i]+nums[j]+nums[z] == 0):
        #                 # res.append([nums[i], nums[j], nums[z]])
        #                 groupset = sorted([nums[i], nums[j], nums[z]])
        #                 if (groupset not in res):
        #                     res.append(groupset)

        # 双指针，先排序，后执行两层遍历，一层为确定数，另一层为双指针两端遍历，你妈的又超时？？？
        # length = len(nums)
        # nums.sort()
        # res = []
        # for i in range(1, length-1):
        #     l = 0
        #     r = length-1
        #     # 左右指针分布在i两侧
        #     while (l < i and r > i):
        #         sums = nums[i]+nums[l]+nums[r]
        #         if (sums == 0):
        #             # 虽然不太清楚为什么，但是似乎没有重复的问题
        #             groupset = [nums[i], nums[l], nums[r]]
        #             if (groupset not in res):
        #                 res.append(groupset)
        #             r -= 1
        #             l += 1
        #             continue

        #         if (sums > 0):
        #             r -= 1

        #         if (sums < 0):
        #             l += 1

        # return res

        # 题解双指针，不想研究了，滚吧傻逼题
        nums.sort()
        res, k = [], 0
        for k in range(len(nums) - 2):
            if nums[k] > 0:
                break  # 1. because of j > i > k.
            if k > 0 and nums[k] == nums[k - 1]:
                continue  # 2. skip the same `nums[k]`.
            i, j = k + 1, len(nums) - 1
            while i < j:  # 3. double pointer
                s = nums[k] + nums[i] + nums[j]
                if s < 0:
                    i += 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                elif s > 0:
                    j -= 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
                else:
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1
        return res

        # @lc code=end


a = Solution()
b = a.threeSum([0, 1, 2, 3, 4, -1, -4, -3, -5, 5, 6, -3, -3, 6])
print(b)
