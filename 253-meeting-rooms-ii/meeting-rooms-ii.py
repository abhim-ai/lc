class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        starts=sorted([start for start,end in intervals])
        ends=sorted([end for start,end in intervals])

        rooms,max_rooms,end_index=0,0,0

        for start in starts:
            if start>=ends[end_index]:
                end_index+=1
            else:
                rooms+=1
            max_rooms=max(rooms,max_rooms)

        return max_rooms

