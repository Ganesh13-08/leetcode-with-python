class Solution:
    def isHappy(self, n: int) -> bool:
        x = n
        add1 = 0
        if n==7:
            return True
        while x>=10:
            add = 0
            while x>0:
                rem = x%10
                add += rem**2
                x = x//10
            x = add
            if x==7:
                return True
        return x==1
            