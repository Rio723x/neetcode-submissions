class Solution:

    def helper(self, index, nums, mem):

        if index >= len(nums):
            return 0

        if mem[index] != -1:
            return mem[index]

        take = nums[index] + self.helper(index + 2, nums, mem)

        not_take = self.helper(index + 1, nums, mem)

        mem[index] = max(take, not_take)

        return mem[index]

    def rob(self, nums: List[int]) -> int:

        mem = [-1] * len(nums)

        return self.helper(0, nums, mem)




            



        