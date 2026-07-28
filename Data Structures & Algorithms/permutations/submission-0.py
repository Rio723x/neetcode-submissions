class Solution:
    def helper(self , visited , path , nums , result):
        if len(path) == len(nums):
            result.append(path[:])
            return 
        
        for i in range(len(nums)):
            if visited[i] == True:
                continue
            path.append(nums[i])
            visited[i] = True

            self.helper( visited , path , nums , result )
        
            path.pop()
            visited[i] =  False

        
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        visited =[False]*len(nums)
        self.helper( visited , path , nums , result)
        return result