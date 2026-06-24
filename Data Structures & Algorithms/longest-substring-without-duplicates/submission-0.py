class Solution:
    def lengthOfLongestSubstring(self, nums: str) -> int:
        seen = set()
        i=0
        max_len = 0
        for j in range(len(nums)):

            while nums[j] in seen:
                seen.remove(nums[i])
                i+=1
            
            seen.add(nums[j])
            
            max_len = max(max_len , j -i + 1)
        return max_len

