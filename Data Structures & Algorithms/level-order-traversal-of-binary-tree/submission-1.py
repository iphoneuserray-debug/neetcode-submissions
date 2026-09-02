# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        left = self.levelOrder(root.left)
        right = self.levelOrder(root.right)
        existed = [x + y for x, y in zip_longest(left, right, fillvalue=[])]
        existed.insert(0, [root.val])
        return existed
        
        
        