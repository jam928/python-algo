
"""

example facts:
 m = 3.28 ft
 ft = 12 in
 hr = 60 min
 min = 60 sec

example queries:
 2m =    ? in   -- > answer = 78.72 in
 13in  = ? m  --> answer = 0.330 m
 13in =  ? hr --> "not convertible"
"""
from collections import defaultdict, deque
from pprint import pprint

"""
    {
        m -> [3.28 ft]
        ft -> [0.3048 m, 12 in]
        in -> [0.08333 ft]
        hr -> [60 min]
        min -> [0.01666 hr, 60 sec]
        sec -> [0.01666 min]
    }
"""

def helper(original_number, original_unit, unit_to_convert_to, facts_map):

    q = deque()
    visited = set()
    q.append((original_number, original_unit))

    while q:
        (current_number, current_unit) = q.popleft()

        if current_unit == unit_to_convert_to:
            return f"{current_number} {unit_to_convert_to}"

        visited.add(current_unit)

        for (other_number, other_unit) in facts_map[current_unit]:
            if other_unit in visited:
                continue
            q.append((current_number * other_number, other_unit))

    return "not convertible"




if __name__ == '__main__':
    facts = ["m=3.28 ft", "ft=12 in", "hr=60 min", "min=60 sec"]

    facts_map = defaultdict(list)

    for fact in facts:
        unit = fact.split("=")[0]
        converts_to_num = float(fact.split("=")[1].split(" ")[0])
        convert_unit = fact.split("=")[1].split(" ")[1]
        facts_map[unit].append((converts_to_num, convert_unit))
        facts_map[convert_unit].append((1/converts_to_num, unit))

    pprint(facts_map)

    queries = ["2 m = ? in", "13 in = ? m", "13 in = ? hr"]
    # queries = ["2 m = ? in"]
    for query in queries:
        original_number = float(query.split(" ")[0])
        original_unit = query.split(" ")[1]
        unit_to_convert_to = query.split(" ")[4]
        print(helper(original_number, original_unit, unit_to_convert_to, facts_map))
