class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: (interval[0], -interval[1]))
        count=0
        maxend=-1
        for start,end in intervals:
            if end>maxend:
                count+=1
                maxend=end
        return count
