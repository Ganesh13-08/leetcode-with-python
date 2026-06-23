class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        lst = nums1 + nums2
        add = 0
        lst = sorted(lst)
        n = len(lst)
        mid = n//2

        if n%2==1:
            return lst[mid]
        else:
            return (lst[mid-1]+lst[mid])/2