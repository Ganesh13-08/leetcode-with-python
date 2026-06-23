class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == -2147483648 and divisor==-1:
            return 2147483647
        elif dividend == -2147483648 and divisor == 1:
            return -2147483648
        else:
            res = dividend/divisor
            res = int(res)
            return res
        