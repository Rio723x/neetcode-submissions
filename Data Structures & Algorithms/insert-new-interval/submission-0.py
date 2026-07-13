class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
            intervals.append(newInterval)

            # move inserted interval to correct position
            for i in range(len(intervals)-1):
                if intervals[i][0] > intervals[-1][0]:
                    intervals[i], intervals[-1] = intervals[-1], intervals[i]

            # merge
            i = 0
            while i < len(intervals)-1:

                if intervals[i][1] >= intervals[i+1][0]:

                    merged = [
                        min(intervals[i][0], intervals[i+1][0]),
                        max(intervals[i][1], intervals[i+1][1])
                    ]

                    intervals.pop(i+1)
                    intervals.pop(i)

                    intervals.insert(i, merged)

                else:
                    i += 1

            return intervals
        