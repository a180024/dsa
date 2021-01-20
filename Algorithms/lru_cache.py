class LinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRU_Cache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dict = {}  # key:node
        self.head = LinkedListNode(0, 0)  # dummy
        self.tail = LinkedListNode(-1, -1)  # dummy
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.dict.get(key, None)
        if node:
            self.removeFromList(node)
            self.insertToHead(node)
            return node.value
        return -1

    def removeFromList(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insertToHead(self, node):
        headNext = self.head.next
        self.head.next = node
        node.next = headNext
        node.prev = self.head
        headNext.prev = node

    def removeFromTail(self):
        if len(self.dict) == 0:
            return
        tailNode = self.tail.prev
        del self.dict[tailNode.key]
        self.removeFromList(tailNode)

    def put(self, key: int, value: int) -> None:
        node = self.dict.get(key, None)
        if node:
            self.removeFromList(node)
            self.insertToHead(node)
            node.value = value
        else:
            if len(self.dict) >= self.capacity:
                self.removeFromTail()
            newNode = LinkedListNode(key, value)
            self.addToHead(newNode)
            self.dict[key] = newNode
