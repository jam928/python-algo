from collections import OrderedDict
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    preqs_map = {}

    for prereq in prerequisites:
        preq_list = preqs_map.get(prereq[0], [])
        preq_list.append(prereq[1])
        preqs_map[prereq[0]] = preq_list

    visited = set()
    ordered_dict = OrderedDict()
    for course in range(0, num_courses):
        if cycle(preqs_map, visited, course, ordered_dict):
            return []
        ordered_dict[course] = None

    ordered_list = list(ordered_dict.keys())
    return ordered_list

def cycle(preqs_map, visited, course, ordered_dict):
    if course in visited:
        return True

    preq_list = preqs_map.get(course, [])

    # if the list of preqs is empty thus no cycle
    if preq_list is None or len(preq_list) == 0:
        return False

    visited.add(course)
    # dfs and check for cycle
    for preq in preq_list:
        if cycle(preqs_map, visited, preq, ordered_dict):
            return True
        ordered_dict[preq] = None

    # remove the course from visited set and preq list as already visited
    if course in visited:
        visited.remove(course)
    if course in preqs_map:
        del preqs_map[course]

    return False

print(find_order(num_courses = 2, prerequisites = [[1,0]])) # [0,1]
print(find_order(num_courses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]])) # [0,1,2,3]
print(find_order(num_courses = 1, prerequisites = [])) # [0]