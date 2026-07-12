class Solution:
    def helper( self , i , j ,dp , m , n ):
        if i == m-1 and j == n-1 :
            return 1

        if i >= m or j >=n:
            return 0
        
        if dp[i][j] != -1:
            return dp[i][j]
        
        #traversal
        down = self.helper(i+1, j , dp , m , n)
        right = self.helper(i, j+1 , dp , m , n )

        dp[i][j] = down + right

        ##ways = max(up or down or left or right)
        return dp[i][j]

        
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1]*(n+1) for _ in range (m+1)]
        return self.helper( 0 , 0 , dp , m , n)