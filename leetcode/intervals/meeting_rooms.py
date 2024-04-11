import heapq

class MeetingRooms:

    def min_meeting_rooms(self, intervals):

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        # add end time elements in min heap
        pq = []

        for interval in intervals:
            if len(pq) != 0 and interval[0] >= pq[0]:
                heapq.heappop(pq)
            heapq.heappush(pq, interval[1])

        return len(pq)

    def can_attend_meetings(self, intervals):

        # sort by start time
        intervals.sort(key=lambda x: x[0])

        for i in range(1, len(intervals)):
            # overlap
            if intervals[i-1][1] > intervals[i][0]:
                return False

        return True


if __name__ == '__main__':
    intervals = [[0,30], [5,10], [15,20]]

    meeting_rooms = MeetingRooms()
    print(meeting_rooms.can_attend_meetings(intervals)) # False
    print(meeting_rooms.min_meeting_rooms(intervals)) # 2

    intervals2 = [[7,10], [2,4]]
    print(meeting_rooms.can_attend_meetings(intervals2)) # True
    print(meeting_rooms.min_meeting_rooms(intervals2)) # 1

