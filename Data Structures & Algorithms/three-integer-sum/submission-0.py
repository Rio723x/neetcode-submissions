class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=set()
        nums.sort()
        for i in range(len(nums)):
            j=i+1
            k=len(nums)-1
            target = -nums[i]

            while j<k:
                curr = nums[j] + nums[k]
                if curr == target:
                    ans.add((nums[i],nums[j],nums[k]))
                    k-=1
                    j+=1
                elif curr < target :
                    j+=1
                else:
                    k-=1
        return [list(x) for x in ans]