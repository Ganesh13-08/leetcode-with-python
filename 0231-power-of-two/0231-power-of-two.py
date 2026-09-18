class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        x = n

        count = 0
        while x>0:
            x = x//2
            count+=1
        return 2**(count-1)==n