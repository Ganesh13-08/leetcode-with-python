class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for i in s:
            if not i.isalpha() and not i.isdigit():
                s = s.replace(i,"")
        new = s[::-1]
        if s==new:
            return True
        else:
            return False