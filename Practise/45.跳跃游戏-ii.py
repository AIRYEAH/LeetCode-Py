#
# @lc app=leetcode.cn id=45 lang=python3
#
# [45] 跳跃游戏 II
#
# 做题次数：1
# @lc code=start
class Solution:
    def jump(self, nums: list[int]) -> int:
        length = len(nums)

        # 单个元素或没有元素的情况
        if (length <= 1):
            return 0

        # 起始遍历点为下标1至下标1对应值所在的下标
        leftIndex = 1
        rightIndex = nums[0]
        step = 1

        # 下标从0号元素开始，根据0号元素对应值，划分出后续可到达的元素区间，从中选取能抵达的最远点
        while rightIndex < length-1:
            for i in range(leftIndex, rightIndex+1):
                if nums[i]+i > rightIndex:
                    rightIndex = nums[i]+i
                    leftIndex = i+1
            step += 1

        return step
        # 失败方法
        # maxDis = 0
        # lenth = len(nums)
        # step = 0
        # if (lenth <= 1):
        #     return 0

        # for i in range(0, lenth):
        #     preDis = nums[i]+i

        #     if (preDis >= lenth-1):
        #         step += 1
        #         return step

        #     if (preDis > maxDis):
        #         maxDis = preDis
        #         step += 1

        # return step
        # 失败方法
        # length = len(nums)
        # step = 0
        # i = 0
        # for i in range(0, length):
        # 难用的for循环，难以在遍历过程中修改迭代遍历，死开

        # # 第一个元素可以直接到达最后的情况
        # if (nums[0] == 0):
        #     return 0

        # if (nums[0] >= length-1):
        #     return 1

        # while (i < length):
        #     currentIndex = i
        #     val = nums[i]
        #     # 获取未来几步的选择，并取最大值
        #     nextchoice = nums[i+1:val+i+1]
        #     if (nextchoice == []):
        #         break

        #     maxInChoice = max(nextchoice)
        #     if (len(nextchoice) <= 1):
        #         i += 1
        #         step += 1
        #         continue

        #     for j in range(0, len(nextchoice)):
        #         if (nextchoice[j]+i >= length):
        #             return step+1

        #         if (nextchoice[j] == maxInChoice):
        #             i = currentIndex+j+1
        #             # i = i + j + 1

        #     step += 1
        #     if (i >= length-1):
        #         break

        # return step
        # @lc code=end


a = Solution()
b = a.jump([7, 0, 9, 6, 9, 6, 1, 7, 9, 0, 1, 2, 9, 0, 3])
print(b)
