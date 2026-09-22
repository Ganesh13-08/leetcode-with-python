class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi = -10**9
        add = 0
        for i in range(len(nums)):
            add += nums[i]
            if add>maxi:
                maxi = add
            if add<0:
                add = 0
        if maxi>=0:
            return maxi
        else:
            return max(nums)
