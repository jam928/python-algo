# https://leetcode.com/problems/min-stack/
class MinStack:

    def __init__(self):
        # Main stack to store elements
        self.stack = []
        # Auxiliary stack to keep track of the minimum element
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if the min stack is empty or the new value is smaller than the current min
        # push the new value to the min stack as the new min
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        # pop the top element from the main stack
        popped = self.stack.pop()

        # if the popped element is the current minimum, also pop it from the min stack
        if popped == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        # return the top element of the main stack
        return self.stack[-1]

    def get_min(self) -> int:
        # return the current min of the min stack
        return self.min_stack[-1]


if __name__ == '__main__':
    # Your MinStack object will be instantiated and called as such:
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.get_min())  # return -3
    min_stack.pop()
    print(min_stack.top())  # return 0
    print(min_stack.get_min())  # return 2
