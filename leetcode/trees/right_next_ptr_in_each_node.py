from collections import deque


def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    if not root:
        return root

    q = deque()

    q.append(root)

    while q:
        level_size = len(q)

        for i in range(level_size):
            curr = q.popleft()

            if len(q) != 0 and i + 1 != level_size:
                curr.next = q[0]
            else:
                curr.next = None

            # append the left and right nodes to the q
            if curr.left:
                q.append(curr.left)

            if curr.right:
                q.append(curr.right)

    return root

