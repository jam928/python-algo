import heapq

class MeetingRooms:

    # II
    def min_meeting_rooms(self, intervals) -> int:
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])

        result = count = 0
        s = e = 0

        while s < len(intervals):
            if start[s] < end[e]:
                s += 1
                count += 1
            else:
                e += 1
                count -= 1

            result = max(result, count)

        return result

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

    meeting_rooms = MeetingRooms()
    print(meeting_rooms.can_attend_meetings(intervals)) # False
    print(meeting_rooms.min_meeting_rooms(intervals)) # 2

    intervals2 = [[7,10], [2,4]]
    print(meeting_rooms.can_attend_meetings(intervals2)) # True
    print(meeting_rooms.min_meeting_rooms(intervals2)) # 1

