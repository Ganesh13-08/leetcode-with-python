class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        result = "".join(str(x)for x in digits)
        result = int(result) + 1
        result = str(result)
        new = [int(ch)for ch in result]
        return new
        