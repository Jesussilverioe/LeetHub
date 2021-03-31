class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        def dfs(path, target, index):
            if target == 0:
                res.append(path)
                return 
            if target < 0:
                return
            for i in range(index, len(candidates)):
                dfs(path+[candidates[i]],target-candidates[i], i)
            
            return path
        
        dfs([],target,0)

        return res