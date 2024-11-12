from random import choice


class RandomizedSet:

    def __init__(self):
        self.dict = {}  # store num -> index
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dict:
            return False

        self.dict[val] = len(self.list)
        self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.dict:
            return False

        val_index = self.dict[val]
        last_num = self.list[-1]

        # swap both numbers to pop in O(1) operation
        self.list[val_index] = last_num

        # pop from last num
        self.list.pop()

        # update map
        self.dict[last_num] = val_index
        del self.dict[val]

        return True

    def getRandom(self) -> int:
        return choice(self.list)

