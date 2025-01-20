import heapq

class MeetingRooms:

    # II
    # T: O(N LOG N)
    # S: O(N)
    def min_meeting_rooms(self, intervals) -> int:
        intervals.sort(key=lambda x: x[0])
        pq = []

        min_meeting_rooms = float('-inf')

        for interval in intervals:
            # pop out elements in q such that the current start time is gte the min time of pq
            while pq and interval[0] >= pq[0]:
                heapq.heappop(pq)

            heapq.heappush(pq, interval[1])
            min_meeting_rooms = max(min_meeting_rooms, len(pq))

        return min_meeting_rooms

    # 1
    def can_attend_meetings(self, intervals) -> bool:

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            # overlap
            if intervals[i-1][1] > intervals[i][0]:
                return False

        return True


if __name__ == '__main__':
    intervals = [[0,30], [5,10], [15,20]]

    # [0,5,15] [10, 20, 30]
    meeting_rooms = MeetingRooms()
    print(meeting_rooms.can_attend_meetings(intervals)) # False
    print(meeting_rooms.min_meeting_rooms(intervals)) # 2

    intervals2 = [[7,10], [2,4]]
    print(meeting_rooms.can_attend_meetings(intervals2)) # True
    print(meeting_rooms.min_meeting_rooms(intervals2)) # 1

