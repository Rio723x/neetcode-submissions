class Solution:
    def helper( self , i , res , nums , result):
        if i == len(nums):
            result.append(res[:])
            return
        #take
        res.append(nums[i])
        self.helper( i + 1 , res , nums , result)
        res.pop()

        while i+1 < len(nums) and nums[i] == nums[i+1]:
            i+=1
        #not_Take
        self.helper( i+1 , res , nums , result)

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        self.helper( 0 , [] , nums , result)
        return result
