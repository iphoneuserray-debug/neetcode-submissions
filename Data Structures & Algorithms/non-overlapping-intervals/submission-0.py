class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = 0
        intervals.sort()
        preEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= preEnd:
                preEnd = end
            else:
                preEnd = min(end, preEnd)
                res += 1
        return res