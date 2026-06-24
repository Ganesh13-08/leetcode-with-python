class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in s:
            if not i.isalnum():
                s = s.replace(i,"")
        new = s[::-1]
        return new == s