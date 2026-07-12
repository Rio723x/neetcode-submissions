class Solution:
    def helper( self , nums , i , dp):
        if i == len(nums)-1:
            return True
        if i > len(nums)-1:
            return False
        
        if dp[i] != -1:
            return dp[i]

        #main loop
        for j in range(1 , nums[i]+1 ):
            if self.helper(nums , i+j , dp):
                dp[i] = True
                return True
        
        dp[i] = False
        return False


    def canJump(self, nums: List[int]) -> bool:
        dp = [False]*(len(nums)+1)
        dp[len(nums)-1] =  True

        for i in range ( len(nums)-1 , -1 , -1 ):
            for j in range( 1 , nums[i] + 1):
                if i+j < len(nums) and dp[i+j]:
                    dp[i] = True
                    break
                    #return dp[i]
        return dp[0]
        #return self.helper( nums , 0 , dp)
            