class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        margelist = nums1 + nums2
        quo, remi = divmod(len(margelist),2)
        if remi:
            return sorted(margelist)[quo]
        return sum(sorted(margelist)[quo -1:quo +1])/2