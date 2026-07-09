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
        if len(nums) == 1:
            return nums[0]
        mem_1 = [-1] * (len(nums) -1)
        mem_2 = [-1] * (len(nums) -1)
        exclude_1 = self.helper(0, nums[:-1], mem_1)
        exclude_2 = self.helper(0 , nums[1:] , mem_2)
        return max(exclude_1 , exclude_2)



            



        