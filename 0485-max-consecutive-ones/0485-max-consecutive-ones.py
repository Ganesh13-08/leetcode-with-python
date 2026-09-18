class Solution:
    def findMaxConsecutiveOnes(self, nums: list[int]) -> int:
        lst = []
        count = 0
        for i in nums:
            if i==1:
                count+=1
            else:
                lst.append(count)
                count = 0
        lst.append(count)
        return max(lst)        