from collections import Counter

# https://leetcode.com/problems/sort-characters-by-frequency/description/

def frequency_sort(s: str) -> str:
    freq_map = Counter(s)

    # sort freq map by value in desc order
    sorted_freq_map = dict(sorted(freq_map.items(), key=lambda x: x[1], reverse=True))

    result = ""
    for k in sorted_freq_map.keys():
        result += k * sorted_freq_map[k]

    return result

if __name__ == '__main__':
    print(frequency_sort("tree")) # eert
    print(frequency_sort("cccaaa")) # cccaaa
    print(frequency_sort("Aabb")) # bbAa