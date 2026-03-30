class ListNode:
    def __init__(self, key = -1, val = -1, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.map = [ListNode() for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        key %= 1000
        if not self.map[key].next: # Start new list
            self.map[key].next = ListNode(key, value)
        else:
            # Check all (except last) nodes in the list
            itr = self.map[key].next
            while itr.next:
                if itr.key == key:
                    itr.val = value
                    return
                itr = itr.next

            # Check the last node in the list
            if itr.key == key:
                itr.val = value
                return

            # Add the new node at the end of the list
            itr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        key %= 1000
        if not self.map[key].next:
            return -1

        # Iterate over the whole list
        itr = self.map[key].next
        while itr:
            if itr.key == key:
                return itr.val
            itr = itr.next

        # Key not found
        return -1


    def remove(self, key: int) -> None:
        key %= 1000
        if not self.map[key].next:
            return

        # Iterate over the whole list
        itr = self.map[key]
        while itr.next:
            if itr.next.key == key:
                itr.next = itr.next.next
                return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)