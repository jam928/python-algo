from typing import List

# https://leetcode.com/problems/queue-reconstruction-by-height/
# T: O(N ^ 2)
# S: O(N)

def reconstruct_queue(people: List[List[int]]) -> List[List[int]]:
    # Sort the people array by height in descending order.
    # If heights are equal, sort by the number of people in front in ascending order.
    people.sort(key=lambda x: (-x[0], x[1]))

    # Create an empty list to store the ordered queue.
    ordered = []
    for p in people:
        # Insert the person at the index specified by their 'k' value.
        ordered.insert(p[1], p)

    return ordered

if __name__ == '__main__':
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(reconstruct_queue(people)) # [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]

    people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]
    print(reconstruct_queue(people)) # [[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]