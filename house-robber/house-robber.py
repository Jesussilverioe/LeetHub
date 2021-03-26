class Solution:
    def rob(self, nums: List[int]) -> int:
        val1= 0
        val2 = 0
        for house in nums:
            t = max(val1 + house, val2)
            val1 = val2
            val2 = t
        return val2
            