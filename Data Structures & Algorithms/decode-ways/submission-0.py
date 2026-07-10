class Solution:
    def helper(self , i , s , dp ):
        if i == len(s):
            return 1
        if s[i] == '0':
            return 0
        
        if dp[i] != -1:
            return dp[i]

        ways  = 0

        #take 1 
        ways = ways + self.helper(i+1 , s , dp)

        #take 2

        if ((i+1 < len(s)) and (10 <= int(s[i:i+2]) <= 26)):
            ways = ways + self.helper( i+2 , s , dp)

        dp[i] = ways
        return dp[i]

    def numDecodings(self, s: str) -> int:
        dp = [-1]*len(s)
        return self.helper(0 , s , dp)
        