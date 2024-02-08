class DoubleLLNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.head = DoubleLLNode()
        self.tail = DoubleLLNode()

        self.head.next = self.tail
        self.tail.prev = self.head

    def _delete_node(self, node: DoubleLLNode):
        # node_prev <-> current_node <-> next_node
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node: DoubleLLNode):
        # head <-> current_node <-> head.next
        node.next = self.head.next
        node.next.prev = node
        node.prev = self.head
        self.head.next = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache.get(key)
        result = node.value

        # delete the node in the list and add it to the to head
        # as most freq used
        self._delete_node(node)
        self._add_to_head(node)

        return result

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self._delete_node(node)
            self._add_to_head(node)
        else:
            # add to map and list
            node = DoubleLLNode(key, value)
            self.cache[key] = node

            if len(self.cache) <= self.capacity:
                self._add_to_head(node)
            else:
                del self.cache[self.tail.prev.key]
                self._delete_node(self.tail.prev)
                self._add_to_head(node)