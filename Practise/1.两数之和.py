#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # lenth = len(nums)
        # hash_table = {}  # 哈希表，存储类型为（数，数在数组中的下标）
        # for i in range(0, lenth):
        #     another = target-nums[i]  # 补数
        #     if (another in hash_table):
        #         return [i, hash_table[another]]  # 返回当前数与补数的下标
        #     hash_table[nums[i]] = i

        # return []
        table = {}
        for i in range(0, len(nums)):
            c = target-nums[i]  # 计算补数
            if (c in table):
                return [table[c], i]

            table[nums[i]] = i  # 将当前数的下标填入表中，便于后续匹配查询

        return []
# @lc code=end


a = Solution()
b = a.twoSum([2, 7, 11, 15], 9)
print(b)
