class Solution:
    def addBinary(self, a: str, b: str) -> str:
        digit = int(a,2) + int(b,2)
        binary = bin(digit)[2:]
        return binary
        