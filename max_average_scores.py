from collections import defaultdict


def max_average_scores(marks):
    average_map = {}

    for mark in marks:
        mark = list(mark)
        score = 0
        name = ""
        if mark[0][0].isdigit():
            score = int(mark[0])
            name = mark[1]
        else:
            score = int(mark[1])
            name = mark[0]

        tuple_to_modified = average_map.get(name, [0, 0])

        tuple_to_modified[0] += 1

        tuple_to_modified[1] += score

        average_map[name] = tuple_to_modified

    print(average_map)

    name = ""
    highest = 0

    # get the max score
    for key, value in average_map.items():
        average = value[1] / value[0]

        if average > highest:
            highest = average
            name = key

    return name

print(max_average_scores([{"Bob","87"}, {"Mike", "35"},{"Bob", "52"}, {"Jason","35"}, {"Mike", "55"}, {"Jessica", "99"}]))