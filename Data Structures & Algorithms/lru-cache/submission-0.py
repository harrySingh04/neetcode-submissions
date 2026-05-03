class Node:

    def __init__(self, key, value):
        self.key  = key
        self.value = value
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

    
    def remove(self ,node):

        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev

    def insert(self, node):

        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        self.tail.prev = node
        node.next = self.tail


    def get(self, key: int) -> int:

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.insert(node)
            return node.value
        
        return -1
        

    def put(self, key: int, value: int) -> None:

        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
        
        node = Node(key,value)
        self.cache[key] = node
        self.insert(node)


        if len(self.cache) > self.capacity:
            # remove head from the doubly linked list 
            lru = self.head.next
            node = self.cache[lru.key]
            self.remove(node)
            del self.cache[lru.key]



        
