class Solution:
    
    def helper_func(self, i , nums , k , curr , ans ):
        if k == 0:
            ans.append(curr.copy())
            return
        if i >= len(nums):
            return
        
        #take 
        if(nums[i] <= k):
            curr.append(nums[i])
            self.helper_func(i , nums , k - nums[i] , curr , ans)
            #self.helper_func( i , nums , k - nums[i] , curr , ans )
            curr.pop()
        
        #not take
        self.helper_func( i + 1 , nums , k , curr, ans)



    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        self.helper_func( 0 , nums , target , [] , ans)
        return ans

        
        