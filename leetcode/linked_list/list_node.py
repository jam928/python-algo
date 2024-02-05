class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        curr = self
        list_of_numbers = []
        while curr:
            list_of_numbers.append(str(curr.val))
            curr = curr.next
        return "[" + ", ".join(list_of_numbers) + "]"
