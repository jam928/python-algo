from collections import defaultdict, deque
from typing import List

# https://leetcode.com/problems/word-ladder/description/
# T: O(n * L^2)
# S: O(n * L^2)


def ladder_length(begin_word: str, end_word: str, word_list: List[str]) -> int:
    g_pattern_map = defaultdict(list)

    for word in word_list:
        for i in range(len(word)):
            pattern = word[0:i] + "*" + word[i + 1:]
            g_pattern_map[pattern].append(word)

    visited = set()
    dq = deque()
    visited.add(begin_word)
    dq.append(begin_word)

    count = 1
    while dq:
        len_of_dq = len(dq)
        for i in range(len_of_dq):
            word = dq.popleft()

            if word == end_word:
                return count

            for j in range(len(word)):
                pattern = word[0:j] + "*" + word[j + 1:]

                for neighbor in g_pattern_map[pattern]:
                    if neighbor in visited:
                        continue
                    visited.add(neighbor)
                    dq.append(neighbor)
        count += 1

    return 0


if __name__ == '__main__':
    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log", "cog"]
    print(ladder_length(begin_word, end_word, word_list))  # 5

    begin_word = "hit"
    end_word = "cog"
    word_list = ["hot", "dot", "dog", "lot", "log"]
    print(ladder_length(begin_word, end_word, word_list))  # 0
