
# https://leetcode.com/problems/implement-queue-using-stacks/
class MyQueue:

    def __init__(self):
        self.stack = []
        self.aux = []

    def push(self, x: int) -> None:
        # push everything from stack1 onto stack2
        while len(self.stack) != 0:
            self.aux.append(self.stack.pop())

        self.stack.append(x)

        # push everything back to stack 1
        while len(self.aux) != 0:
            self.stack.append(self.aux.pop())

    def pop(self) -> int:
        return self.stack.pop() if len(self.stack) != 0 else -1

    def peek(self) -> int:
        return self.stack[-1] if len(self.stack) != 0 else -1

    def empty(self) -> bool:
        return True if len(self.stack) == 0 else False


if __name__ == '__main__':
    my_q = MyQueue()
    my_q.push(1)
    my_q.push(2)
    print(my_q.peek()) # 1
    print(my_q.pop()) # 1
    print(my_q.empty()) # False