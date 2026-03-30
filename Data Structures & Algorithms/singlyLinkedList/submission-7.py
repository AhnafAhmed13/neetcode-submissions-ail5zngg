class Node:
    def __init__(self, value=0):
        print("initialize node")
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        print("initialize LL")
        self.head = None
        self.tail = self.head
    
    def get(self, index: int) -> int:
        print("get", index)
        itr = self.head
        count = 0
        while itr:
            if count == index:
                print(itr.value)
                return itr.value
            itr = itr.next
            count += 1
        print(-1)
        return -1

    def insertHead(self, val: int) -> None:
        print("insertHead", val)
        node = Node(val)
        node.next = self.head
        self.head = node

    def insertTail(self, val: int) -> None:
        print("insertTail", val)
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node
            return

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = node
        self.tail = node

    def remove(self, index: int) -> bool:
        print("remove", index)
        if not self.head:
            print(False)
            return False

        if index == 0:
            self.head = self.head.next
            print(True)
            return True

        count = 0
        itr = self.head
        while itr.next:
            if count == index - 1:
                if itr.next.next:
                    itr.next = itr.next.next
                else:
                    itr.next = None
                    self.tail = itr
                print(True)
                return True
            itr = itr.next
            count += 1
        print(False)
        return False

    def getValues(self) -> List[int]:
        print("getValues")
        values = []
        itr = self.head
        while itr:
            values.append(itr.value)
            itr = itr.next
        print(values)
        return values
