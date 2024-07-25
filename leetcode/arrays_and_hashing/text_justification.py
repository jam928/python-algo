from typing import List

# T: O(n*m) # where n is there number of words and m is the maximum number of words that fit in a line
# S: O(n*m) # where n is there number of words and m is the maximum number of words that fit in a line
# https://leetcode.com/problems/text-justification/

def full_justify(words: List[str], max_width: int) -> List[str]:
    result = []
    current_line = []
    current_length = 0
    i = 0

    while i < len(words):
        # current line complete
        if current_length + len(current_line) + len(
                words[i]) > max_width:  # if current line length plus the spaces plus the current word length
            extra_space = max_width - current_length

            spaces = extra_space // max(1, len(current_line) - 1)
            remainder = extra_space % max(1, len(current_line) - 1)

            for j in range(max(1, len(current_line) - 1)):
                current_line[j] += " " * spaces

                if remainder:
                    current_line[j] += " "
                    remainder -= 1

            result.append("".join(current_line))
            current_line = []
            current_length = 0

        current_line.append(words[i])
        current_length += len(words[i])
        i += 1

    # handling last line
    last_line = " ".join(current_line)
    trail_space = max_width - len(last_line)
    last_line += " " * trail_space
    result.append(last_line)

    return result
