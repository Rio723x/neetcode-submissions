class Solution:
    def helper( self , index , nums , dp , prevIndex):
        
        if index > len(nums):
            return 0
        if index == len(nums):
            return 0
        if dp[index][prevIndex+1] != -1:
            return dp[index][prevIndex+1]

        #take
        take = 0 
        if prevIndex == -1 or nums[index] > nums[prevIndex]:
            take = 1 + self.helper(index + 1 ,nums,  dp , index)
        
        #not take
        not_take = self.helper(index + 1, nums,  dp , prevIndex)

        dp[index][prevIndex+1] = max( not_take , take)
        return dp[index][prevIndex+1]

    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [[-1]* len(nums) for _ in range (len(nums)+1 )]
        return self.helper(0 , nums , dp , -1 )

        