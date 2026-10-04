"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not len(intervals):
            return True
        intervals.sort(key = lambda x: x.start)
        prevEnd = intervals[0].end
        for time in intervals[1:]:
            
            if time.start < prevEnd:
                return False
            else:
                prevEnd = time.end
        return True