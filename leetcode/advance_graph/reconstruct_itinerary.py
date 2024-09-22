import heapq
from collections import defaultdict, deque
from typing import List


# T: O(nlogn)
# S: O(n)
def find_itinerary(tickets: List[List[str]]) -> List[str]:
    # Create a map with a priority queue for each departure point
    adj_list = defaultdict(list)

    # Build the graph
    for ticket in tickets:
        heapq.heappush(adj_list[ticket[0]], ticket[1])

    q = deque()
    stack = ["JFK"]

    while stack:
        from_ = stack[-1]
        # Poll the least lexicographically element from the current 'from'
        if from_ in adj_list and adj_list[from_]:
            stack.append(heapq.heappop(adj_list[from_]))
        else:
            q.appendleft(stack.pop())

    return list(q)


print(find_itinerary(
    tickets=[["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))  # ["JFK","MUC","LHR","SFO","SJC"]
print(find_itinerary(tickets=[["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"],
                              ["ATL", "SFO"]]))  # ["JFK","ATL","JFK","SFO","ATL","SFO"]
