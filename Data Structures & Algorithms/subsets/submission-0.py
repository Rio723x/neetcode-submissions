class Solution:
    def helper(self , res , i , nums , result):
        if i == len(nums):
            result.append(list(res))
            return
        
        #take
        res.append(nums[i])
        self.helper(res , i+1 , nums , result)
        res.pop()
        
        #not_take
        self.helper( res , i + 1 , nums , result)
    
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.helper([] , 0 , nums , result)
        return result