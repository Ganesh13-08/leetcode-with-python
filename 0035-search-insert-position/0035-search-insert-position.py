class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        found = 0
        end = len(nums)-1
        while(start<=end):
            mid = (start + end)//2
            if nums[mid]==target:
                found = 1
                return mid
            elif nums[mid]>target:
                end = mid-1
            else:
                start = mid+1
        if found==0:
            nums.append(target)
            nums = sorted(nums)
            pos = nums.index(target)
            return pos

        