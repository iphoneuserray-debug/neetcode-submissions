class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True
        visit = set()
        nodes = {i: [] for i in range(n)}
        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        def dfs(num, prev):
            if num in visit:
                return False
            visit.add(num)
            for i in nodes[num]:
                if i == prev:
                    continue
                if not dfs(i, num):
                    return False
            return True
        
        if not dfs(0, -1):
            return False
        if len(visit) < n:
            return False
        return True
            