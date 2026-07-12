class Solution:
    def helper( self , i , j, text1 , text2 , dp ):
        if i == len(text1) or j == len(text2):
            return 0
        if i > len(text1) or j > len(text2):
            return 0

        if dp[i][j] != -1:
            return dp[i][j]

        #check
        if text1[i] == text2[j]:
            #dp[i][j] = 1 + self.helper(i+1,j+1,text1,text2,dp)
            ways = 1 + self.helper(i+1,j+1,text1,text2,dp)

        if text1[i] != text2[j]:
            
            ways = max(self.helper(i+1,j,text1,text2,dp), self.helper(i,j+1,text1,text2,dp))
        
         
        dp[i][j] = ways
        return dp[i][j]

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[-1]* (len(text2)+1) for _ in range(len(text1)+1)]
        return self.helper( 0 , 0 , text1 , text2 , dp )