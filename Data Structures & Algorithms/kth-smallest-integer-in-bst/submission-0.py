# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        smallest value is guaranteed to be leftmost child

        do inorder traversal, and in recursion pass down current k

        k representing the n'th smallest value we're on right now

        then on each node we check if its k
            if it is we update our global variable and return
        """
        kSmallest = None
        def dfs(node):
            nonlocal k
            nonlocal kSmallest

            if not node or kSmallest:
                return
            
            dfs(node.left)

            if k == 1:
                kSmallest = node.val
            k -= 1

            dfs(node.right)
        
        dfs(root)
        return kSmallest