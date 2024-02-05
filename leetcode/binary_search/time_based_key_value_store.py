class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # append (value, timestamp) to the specific key in the map
        time_element_list_tuples = self.time_map.get(key, [])
        time_element_list_tuples.append((value, timestamp))
        self.time_map[key] = time_element_list_tuples

    def get(self, key: str, timestamp: int) -> str:
        time_element_list_tuples = self.time_map.get(key, [])
        result = ""

        # do a binary search on the tuples list timestamp
        # if the timestamp equals at the mid point return that specific value
        # o.w store the result and move the left and right pointers accordingly
        left = 0
        right = len(time_element_list_tuples) - 1

        while left <= right:
            mid = (left + right) // 2

            value = time_element_list_tuples[mid][0]
            current_timestamp = time_element_list_tuples[mid][1]
            if current_timestamp == timestamp:
                result = value
                break

            if current_timestamp <= timestamp:
                result = value
                left = mid + 1
            else:
                right = mid - 1

        return result
if __name__ == '__main__':
    time_map = TimeMap()
    time_map.set("foo", "bar", 1)
    print(time_map.get("foo", 1))  # return "bar"
    print(time_map.get("foo", 3))  # return "bar"
    time_map.set("foo", "bar2", 4)
    print(time_map.get("foo", 4))  # return "bar2"
    print(time_map.get("foo", 5))  # return "bar2"

