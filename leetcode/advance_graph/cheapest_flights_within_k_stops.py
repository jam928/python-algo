import heapq
from collections import defaultdict
from typing import List


# https://leetcode.com/problems/cheapest-flights-within-k-stops/description/
# Time Complexity: O(E + N * log N)
# Space Complexity: O(E + N)

def find_cheapest_price(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # build the adj list
    adj_list = defaultdict(list)

    for u, v, w in flights:
        adj_list[u].append((v, w))

    pq = [(0, src, 0)]  # (price, source, stops)
    cheapest_price = float('inf')
    visited_stops = [n] * n

    while pq:
        current_price, current_source, current_stop = heapq.heappop(pq)

        if current_source not in adj_list:
            continue

        visited_stops[current_source] = current_stop

        for destination, flight_price in adj_list[current_source]:
            new_price = flight_price + current_price
            new_stop = current_stop + 1

            # if the new price is greater than the current cheapest price
            # or if the new stop is greater than k + 1
            # or if new stop is greater than the visited stop at the destination
            # then continue to the next node
            if new_price > cheapest_price or new_stop > k + 1 or new_stop > visited_stops[destination]:
                continue

            # update the cheapest price
            if destination == dst:
                cheapest_price = new_price
                continue

            heapq.heappush(pq, (new_price, destination, new_stop))

    return cheapest_price if cheapest_price != float('inf') else -1


print(find_cheapest_price(n=4, flights=[[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], src=0, dst=3,
                          k=1))  # 700

print(find_cheapest_price(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=1))  # 200

print(find_cheapest_price(n=3, flights=[[0, 1, 100], [1, 2, 100], [0, 2, 500]], src=0, dst=2, k=0))  # 500
