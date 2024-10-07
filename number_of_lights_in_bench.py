import heapq
from functools import cmp_to_key


def compare_func(event1, event2):
    # if the time of the event is not equal then take the greater of the two
    if event1[1] != event2[1]:
        return event1[1] - event2[1]
    # else take the greater two of events
    return event1[0] - event2[0]


def number_of_lamps_illuminating_benches(lamps, benches):
    # 0 - lamp turning on
    # 1 - encountering a bench
    # 2 - lamp turning off

    # [type of event, time of event]
    arr = []
    for lamp in lamps:
        arr.append([0, lamp[0]])
        arr.append([2, lamp[1]])

    # push benches in array as well
    for index, bench in enumerate(benches):
        arr.append([1, bench, index])

    print(arr)

    # sort arr by compare_func
    arr.sort(key=cmp_to_key(compare_func))
    print(f'After sorted: {arr}')
    answer = [0 for _ in range(len(benches))]
    number_of_lamps_lit = 0

    for event in arr:
        if event[0] == 0:
            number_of_lamps_lit += 1
        elif event[0] == 2:
            number_of_lamps_lit -= 1
        else:
            answer[event[2]] = number_of_lamps_lit

    return answer

if __name__ == '__main__':
    # lamps = [[-20, -3], [-10, -1], [-5, 14], [11, 15]]
    # benches = [-17, -10, -4, 4, 12, 16]
    #
    # result = number_of_lamps_illuminating_benches(lamps, benches)
    # print(result) # [1,2,3,1,2,0]

    lamps = [[1,4],[2,4],[3,6],[4,4]]
    benches = [2,3,4,5]

    print(number_of_lamps_illuminating_benches(lamps, benches))