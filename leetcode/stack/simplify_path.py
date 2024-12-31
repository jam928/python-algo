from collections import deque

# https://leetcode.com/problems/simplify-path/

def simplify_path(path: str) -> str:

    # split the string by /
    dirs = path.split("/")
    dq = deque()

    # add each directory to deque
    for directory in dirs:
        if len(directory) == 0 or directory == '.':
            continue
        elif directory == '..':
            if len(dq) != 0:
                dq.pop()
        else:
            dq.append(directory)

    # get the result from deque
    path = ""
    while len(dq) != 0:
        path += "/" + dq.popleft()

    return path if path else "/"

if __name__ == "__main__":
    paths = ["/home/", "/home//foo/", "/home/user/Documents/../Pictures",
             "/../",  "/.../a/../b/c/../d/./"]

    for path in paths:
        print(simplify_path(path))
