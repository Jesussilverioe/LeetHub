# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        if not root: return None
        
        ans = []
        q = collections.deque()
        q.append(root)
        while q:
            qlen = len(q)
            lvl = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    q.append(node.left)
                    q.append(node.right)
                    lvl.append(node.val)
            if lvl:
                ans.append(lvl[-1])
        return ans