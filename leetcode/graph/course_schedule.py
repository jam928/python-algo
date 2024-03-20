from typing import List

# T:O(n + m^2) where n is the number of preqs and m is the number of courses
# S:O(n)
# https://leetcode.com/problems/course-schedule/description/
def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    preqs_map = {}

    for prereq in prerequisites:
        preq_list = preqs_map.get(prereq[0], [])
        preq_list.append(prereq[1])
        preqs_map[prereq[0]] = preq_list

    visited = set()
    for course in range(0, num_courses):
        if cycle(preqs_map, visited, course):
            return False

    return True


def cycle(preqs_map, visited, course):
    if course in visited:
        return True

    preq_list = preqs_map.get(course, [])

    # if the list of preqs is empty thus no cycle
    if preq_list is None or len(preq_list) == 0:
        return False

    visited.add(course)
    # dfs and check for cycle
    for preq in preq_list:
        if cycle(preqs_map, visited, preq):
            return True

    # remove the course from visited set and preq list as already visited
    if course in visited:
        visited.remove(course)
    if course in preqs_map:
        del preqs_map[course]

    return False

print(can_finish(num_courses = 2, prerequisites = [[1,0]])) # True
print(can_finish(num_courses = 2, prerequisites = [[1,0],[0,1]])) # False
