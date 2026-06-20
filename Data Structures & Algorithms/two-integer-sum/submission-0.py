class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        list1=[]
        for i in range (len(nums)):
            x = target - nums[i]
            if x in nums:
                for j in range(i+1,len(nums)):
                    if nums[j]== x:
                        list1.append(i)
                        list1.append(j)
                        return list1
            else:
                continue

