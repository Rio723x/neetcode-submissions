class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            left = i
            right = i
            while left >=0 and right < len(s) and s[left] == s[right]:
                right +=1
                left -=1
                res+=1
            #curr = s[left+1:right]
            #if len(curr) > len(res):
            #   res = curr

            left = i
            right = i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                right +=1
                left -=1
                res+=1
        return res