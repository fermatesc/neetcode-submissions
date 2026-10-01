class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = [intervals[0]]
        for i in range(1, len(intervals)):
            last_end = res[-1][1]
            if intervals[i][0] <= last_end:
                res[-1][1] = max(intervals[i][-1], last_end)
            else:
             res.append(intervals[i])
        return res