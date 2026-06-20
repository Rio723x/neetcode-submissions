class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = 1

        zero_count = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero_count += 1
            else:
                ans = ans * nums[i]

        if zero_count == 0:
            for j in range(len(nums)):
                nums[j] = ans // nums[j]

        elif zero_count == 1:
            for j in range(len(nums)):
                if nums[j] == 0:
                    nums[j] = ans
                else:
                    nums[j] = 0

        else:
            for j in range(len(nums)):
                nums[j] = 0

        return nums
        