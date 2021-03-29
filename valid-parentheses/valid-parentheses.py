class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        map = {'}':'{', ')':'(',']':'['}
        
        for char in s:
            if char in map:
                top_char = stack.pop() if stack else '1'
                if map[char] != top_char:
                    return False
            else:
                stack.append(char)
                
        return not stack