class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if k == 0:
            return any(nums[i] == 0 and nums[i+1] == 0 for i in range(len(nums)-1))
        mydic = {0:-1}
        total = 0
        for i, val in enumerate(nums):
            total = (total + val)%k
            if total in mydic and i - mydic[total] > 1:
                return True
            if total not in mydic:
                mydic[total] = i
        return False
                