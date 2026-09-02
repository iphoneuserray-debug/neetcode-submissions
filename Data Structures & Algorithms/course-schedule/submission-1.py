class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for pre, course in prerequisites:
            preMap[course].append(pre)
        vis = set()

        def dfs(i):
            if i in vis:
                return False
            if preMap[i] == []:
                return True
            vis.add(i)
            for node in preMap[i]:
                if not dfs(node):
                    return False
            vis.remove(i)
            preMap[i] = []
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        
        return True