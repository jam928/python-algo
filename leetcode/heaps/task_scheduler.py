
# https://leetcode.com/problems/task-scheduler/

def least_interval(tasks, n):
    # count the frequency of each task
    task_counts = [0] * 26

    for task in tasks:
        task_counts[ord(task) - ord('A')] += 1

    # sort the count in descending order to start with most frequent tasks
    task_counts.sort(reverse=True)

    # Calculate maximum possible idle slots based on the most freq tasks
    max_count = task_counts[0] - 1
    idle_slots = max_count * n

    # iterate over the remaining tasks, subtracting their counts from the idle slots
    for count in task_counts[1:]:
        idle_slots -= min(max_count, count)

    idle_slots = max(0, idle_slots)  # idle slots can not be negative
    return len(tasks) + idle_slots

# Example usage:
tasks = ["A", "A", "A", "B", "B", "C", "C"]
cooldown = 1
print(least_interval(tasks, cooldown))  # Output should be 8