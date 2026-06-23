class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lst = []
        if target in nums:
            if nums.count(target)>=2:
                for i in range(len(nums)):
                    if target == nums[i]:
                        lst.append(i)
                return [lst[0],lst[-1]]
            else:
                return [nums.index(target),nums.index(target)]
        else:
            return [-1,-1]