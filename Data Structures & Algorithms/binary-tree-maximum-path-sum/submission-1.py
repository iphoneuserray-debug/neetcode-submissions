# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxNodes = []
        def dps(root):
            if not root:
                return None
            
            left = dps(root.left)
            right = dps(root.right)
            matrix = [root.val]
            if left:
                matrix.append(left + root.val)
            if right:
                matrix.append(right + root.val)
            if left and right:
                asRoot = right + root.val + left
                maxNodes.append(asRoot)
            max_branch = max(matrix)
            maxNodes.append(max_branch)
            if not root.left and not root.right:
                return root.val
            
            return max_branch
        maxNodes.append(dps(root))
        return max(maxNodes)
        
            