"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        create = {}
        if not node:
            return None
        root = Node()
        root.val = 0

        def dfs(node, root):
            if node.val in create.keys():
                root.neighbors.append(create[node.val])
                return
            cur = Node()
            cur.val = node.val
            create[node.val] = cur
            root.neighbors.append(cur)

            for n in node.neighbors: 
                dfs(n, cur)
        
        dfs(node, root)
        return root.neighbors[0]
            