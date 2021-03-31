class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) == 1:
            return [nums[:]]
        
        for i in range(len(nums)):
            n = nums.pop(0)
            perm = self.permute(nums)
            
            for per in perm:
                per.append(n)
            result.extend(perm)
            nums.append(n)
            
            
        return result