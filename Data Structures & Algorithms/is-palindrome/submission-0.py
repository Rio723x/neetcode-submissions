class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for i in s:
            if i.isalnum():
                new_s += i.lower()

        if new_s == new_s[::-1]:
            return True
        else:
            return False