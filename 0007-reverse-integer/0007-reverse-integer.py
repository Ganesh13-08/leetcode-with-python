class Solution:
    def reverse(self, x: int) -> int:
        if x>0 and x<=2147483647:
            x = str(x)
            x = x[::-1]
            x = int(x)
            if x>=2147483647:
                return 0
            return x
        elif x<0 and x>(-2147483647):
            x = -1*x
            x = str(x)
            x = x[::-1]
            x = -int(x)
            if x<(-2147483647):
                return 0
            return x
        else:
            return 0

        