class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currsum = 0
        if len(nums)==1:
            return nums[0]
        if len(nums)==0:
            return []

        for i in nums:
            if currsum < 0 :
                currsum = 0
            currsum = currsum + i
            maxsum = max(currsum , maxsum)
        return maxsum

        