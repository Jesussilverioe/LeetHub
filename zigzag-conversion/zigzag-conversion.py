class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
    
        templist =  [[] for i in range(numRows)]
        rows = 0
        directions = -1
        for c in s:
            templist[rows].append(c)
            if rows == 0 or rows == numRows-1:
                directions = -directions
            rows += directions
        templist = ''.join([c for r in templist for c in r])
        print(templist)
        return templist