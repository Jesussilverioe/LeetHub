from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p1 = 0
        p2 = len(s1)
        c1 = Counter(s1)
        while p2 < len(s2)+1:
            c2 = Counter(s2[p1:p2])
            if c1 == c2:
                return True
            p1 += 1
            p2 += 1
            
            
        return False