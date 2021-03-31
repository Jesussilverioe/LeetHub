class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0,0
        counted = set()
        long = 0
        while l < len(s) and r < len(s):
            if s[r] not in counted:
                counted.add(s[r])
                r += 1
                long = max(long,r-l)
            else:
                counted.remove(s[l])
                l += 1
                
        return long
                