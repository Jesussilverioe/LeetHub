class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydic = {}
        for i,val in enumerate(nums):
            if target - val in mydic:
                return mydic[target-val],i
            mydic[val] = i
        