#
# @lc app=leetcode.cn id=283 lang=python3
#
# [283] 移动零
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # stack = []
        # nums.sort()
        # start = 0
        # end = 0
        # startTag = False
        # endTag = False
        # for i in range(0, len(nums)):
        #     if (startTag == False and nums[i] == 0):
        #         start = i
        #         startTag = True
        #     if (endTag == False and nums[i] > 0):
        #         end = i
        #         endTag = True
        #     if (startTag and endTag):
        #         break

        # nums = nums[0:start] + nums[end:]+nums[start:end]
        # print(nums)

        # 双指针思路：一个指针用于修改数组内的数，一个指针用于判断是否为0，不为0则将该指针指向地址的对应值传递到上一个指针的对应值中
        length = len(nums)
        if (length <= 1):
            return

        index = 0
        # zeroCount = 0
        for i in range(0, length):
            # 前指针指向数为0时，不执行操作
            if (nums[i] == 0):
                # zeroCount += 1
                continue
            # 前指针指向数已由上一步确定不可能为0，此时将前指针的指向值传递给当前index的指向即可
            if (index < i):
                nums[index] = nums[i]
            index += 1

        # nums = nums[:index]+[0 for i in range(zeroCount)]
        for i in range(index, length):
            nums[i] = 0

        # print(nums)


# @lc code=end
a = Solution()
a.moveZeroes([0, 1, 0, 3, 12])
