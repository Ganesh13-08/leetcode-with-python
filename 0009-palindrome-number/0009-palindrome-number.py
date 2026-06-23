class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = x
        add = 0
        while(n>0):
            add = add*10 + n%10
            n = n//10
        if x==add:
            return True
        else:
            return False