# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    def __init__(self):
        self.times = {} # (city, id) -> (time)
        self.total_trips = {} # (pair) ->  (total, total_trips, average)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # update times map
        self.times[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # update total trips
        source_station, check_in_time = self.times[id]
        time_took = t - check_in_time
        if (source_station, stationName) not in self.total_trips:
            self.total_trips[(source_station, stationName)] = [0, 0]
        self.total_trips[(source_station, stationName)][0] += time_took # update the total time for this pair
        self.total_trips[(source_station, stationName)][1] += 1 # update the total amount of trips of this pair

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.total_trips[(startStation, endStation)][0] / self.total_trips[(startStation, endStation)][1]