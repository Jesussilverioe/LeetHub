class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        for i,val in enumerate(nums):
            if i > 0 and val == nums[i-1]:
                continue
            beg = i + 1
            end = len(nums) - 1
            while beg < end:
                tsum = val + nums[beg] + nums[end]
                if tsum < 0:
                    beg += 1
                elif tsum > 0:
                    end -= 1
                else:
                    res.append([val, nums[beg], nums[end]])
                    beg += 1
                    while nums[beg] == nums[beg-1] and beg < end:
                        beg += 1
                        
        return res
            
                