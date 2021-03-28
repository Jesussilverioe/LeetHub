# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        
        temp = root.right
        root.right = root.left
        root.left = temp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
    #def invertTree2(self, root):
    #    if not root:
    #        return None
    #    stack = [root]
    #    while stack != []:
    #        node = stack.pop()
    #        node.left, node.right = node.right, node.left
    #        if node.left:
    #           stack.append(node.left)
    #        if node.right:
    #            stack.append(node.right)
    #    return root
    
    
    