class Solution:
    def helper( self , nums , currsum , i , sums , dp):
        if i >= len(nums):
            return False
        
        if currsum == sums:
            return True
        
        if currsum > sums:
            return False
        
        if dp[i][currsum] != -1:
            return dp[i][currsum]
        
        #take
        take = self.helper( nums , currsum + nums[i] , i+1 , sums , dp)
        #not take 
        not_take = self.helper( nums , currsum , i+1  , sums , dp )

        dp[i][currsum] =  take or not_take
        return dp[i][currsum]
        
    def canPartition(self, nums: List[int]) -> bool:
        sums = 0
        for j in range(len(nums)):
            sums = sums + nums[j]
        dp = [[-1]*(sums + 1 ) for _ in range(len(nums))]

        if sums % 2 != 0:
            return False
        
        sums = sums // 2
        return self.helper( nums , 0 ,  0, sums , dp) 
        