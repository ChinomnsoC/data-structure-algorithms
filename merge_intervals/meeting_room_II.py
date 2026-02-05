
import heapq
from typing import List

# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # sort interval
        intervals.sort(key=lambda x: x.start)

        # group intervals that have no intersection

        rooms_heap = []


        heapq.heappush(rooms_heap, intervals[0].end)

        for i in range(1, len(intervals)):
            if intervals[i].start >= rooms_heap[0]:
                heapq.heappop(rooms_heap)

            heapq.heappush(rooms_heap, intervals[i].end)
        
        return len(rooms_heap)
        