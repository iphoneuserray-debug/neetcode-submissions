# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return None
        
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        isAim = False
        if root.val == p.val or root.val == q.val:
            isAim = True

        if left and right:
            return  root
        elif isAim and left or isAim and right:
            return root
        elif isAim:
            return root
        elif left:
            return left
        elif right:
            return right
        
        return None