
# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
# T: O(N)
# S: O(1)

def min_add_to_make_valid(s: str) -> int:
    open_count = 0
    min_moves = 0

    for c in s:
        if c == '(':
            open_count += 1
        else:
            if open_count >= 1:
                open_count -= 1
            else:  # we do not have enough open parenthesis so we need add a move
                min_moves += 1

    # if we have any open count remaining include it in min moves
    # as we need it for the close )
    if open_count >= 1:
        min_moves += open_count
    return min_moves

if __name__ == '__main__':
    print(min_add_to_make_valid('())')) # 1
    print(min_add_to_make_valid('(((')) # 3