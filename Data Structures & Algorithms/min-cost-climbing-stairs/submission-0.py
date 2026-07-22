class Solution:
    def helper( self , cost , i , dfs):

        if i >= len(cost):
            return 0

        if dfs[i] != -1:
            return dfs[i]

        
        dfs[i] = cost[i] + min( self.helper(cost , i + 1 , dfs) , self.helper( cost , i + 2 , dfs))
        
        return dfs[i]

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dfs = [-1]*len(cost)

        return min(self.helper(cost , 0 , dfs ) , self.helper(cost , 1 , dfs))
        
        