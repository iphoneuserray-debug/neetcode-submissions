# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def findSmall(root, k):
            if not root:
                return None
            
            left = findSmall(root.left, k)
            if left:
                return left
            if k[0] == 1:
                return root.val
            k[0] -= 1
            return findSmall(root.right, k)
        return findSmall(root, [k])