# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        maybe pre order traversal

        have a max seen variable
        
        if node.val is greater than maxSeen, then tick counter variable
        """
        if not root:
            return 0
        
        res = 0
        def dfs(node, maxSeen):
            if not node:
                return
            
            nonlocal res
            if node.val >= maxSeen:
                res += 1
                maxSeen = node.val
            
            dfs(node.left, maxSeen)
            dfs(node.right, maxSeen)
            
        
        dfs(root, root.val)
        return res