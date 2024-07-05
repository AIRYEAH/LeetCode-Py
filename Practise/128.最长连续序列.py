#
# @lc app=leetcode.cn id=128 lang=python3
#
# [128] 最长连续序列
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # 非哈希表解法，先排序，后逐一和前数比较，存在递增关系则更新长度
        # if (len(nums) == 0):
        #     return 0

        # if (len(nums) == 1):
        #     return 1

        # table = {}
        # nums.sort()
        # index = 0
        # table[0] = 1
        # for i in range(1, len(nums)):
        #     # 下一个元素与前一个元素的差值不为1，说明不连续，应作为新的头元素放入哈希表
        #     if (nums[i-1] == nums[i]):
        #         continue
        #     elif (nums[i-1] != nums[i]-1):
        #         index += 1
        #         table[index] = 1
        #     else:0
        #         table[index] += 1

        # return max(table.values())

        # 哈希表解法,通过集合和一个连续数组的头元素来寻找连续元素长度的办法。巧但不易理解
        res = 0  # 记录最长连续长度
        num_set = set(nums)  # 记录非重复的集合
        for num in num_set:
            if (num-1) not in num_set:
                seq_len = 1
                while (num+1) in num_set:
                    seq_len += 1
                    num += 1

                res = max(res, seq_len)

        return res

        # @lc code=end


a = Solution()
b = a.longestConsecutive([1, 2, 0, 1, 99, 100, 5])
print(b)
