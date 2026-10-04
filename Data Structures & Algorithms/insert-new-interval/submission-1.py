class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ns, ne = newInterval
        res = []
        add = False
        for s, e in intervals:
            
            if ne < s:
                if not add:
                    res.append([ns, ne])
                    add = True
                res.append([s, e])
            elif ns > e:
                res.append([s, e])
            else:
                ns = min(s, ns)
                ne = max(e, ne)
        if not add:
            res.append([ns, ne])
        return res