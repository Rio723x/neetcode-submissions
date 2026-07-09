class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):
            left = i
            right = i
            while left >=0 and right < len(s) and s[left] == s[right]:
                right +=1
                left -=1
            curr = s[left+1:right]
            if len(curr) > len(res):
                res = curr

            left = i
            right = i+1
            while left >=0 and right < len(s) and s[left] == s[right]:
                right +=1
                left -=1

            curr = s[left+1:right]
            if len(curr) > len(res):
                res = curr
        return res
        