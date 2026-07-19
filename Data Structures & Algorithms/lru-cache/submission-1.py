class Node:
    def __init__(self,key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)

        self.head.next = self.tail
        self.tail.prev = self.head
    

    def remove(self,node):
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def add(self, node):
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node

    def evict(self):
        del(self.cache[self.head.next.key])
        self.remove(self.head.next)




        

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
            self.add(node)
        else:
            if len(self.cache) == self.capacity:
                self.evict()
            node = Node(key, value)
            self.cache[key] = node
            self.add(node)

        
