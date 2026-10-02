class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if not n:
            return 0
        visit = set()
        numbers = [i for i in range(n)]
        nodes = {i: [] for i in range(n)}
        tree = 0

        for n1, n2 in edges:
            nodes[n1].append(n2)
            nodes[n2].append(n1)

        def dfs(num, prev):
            if num in visit:
                return
            visit.add(num)
            for i in nodes[num]:
                if i == prev:
                    continue
                dfs(i, num)
            return
        
        for i in numbers:
            if i not in visit:
                dfs(i, -1)
                tree += 1
        return tree