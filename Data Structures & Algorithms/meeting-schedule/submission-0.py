"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:

        def getStart(interval):
            return interval.start

        intervals.sort(key=getStart)

        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False

        return True

