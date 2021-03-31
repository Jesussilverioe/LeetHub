class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i:i[0])
        ans = [intervals[0]]
        for beg,end in intervals[1:]:
            lastval = ans[-1][1]
            if lastval >= beg:
                ans[-1][1] = max(lastval, end)
            else:
                ans.append([beg,end])
        return ans