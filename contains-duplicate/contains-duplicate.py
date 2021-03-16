class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        mydic = {}
        beg = 0
        end = len(nums) - 1
        while beg < end:
            
            if nums[beg] in mydic:
                return True
            mydic[nums[beg]] = 0
            
            if nums[end] in mydic:
                return True
            mydic[nums[end]] = 0
            beg += 1
            end -= 1
            
        return False