class Solution:
    def canAttendMeetings(self, intervals: list[list[int]]) -> bool:
        intervals.sort()
        for i in range(1,len(intervals)):
            prev_end=intervals[i-1][1]
            start=intervals[i][0]
            if start<prev_end:
                return False
        return True
    
       