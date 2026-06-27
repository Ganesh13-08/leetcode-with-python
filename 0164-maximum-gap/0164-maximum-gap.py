class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        lst = []
        nums.sort()
        if not nums or len(nums)<2:
            return 0
        for i in range(len(nums)-1):
            diff = nums[i+1]-nums[i]
            lst.append(diff)
        return max(lst)