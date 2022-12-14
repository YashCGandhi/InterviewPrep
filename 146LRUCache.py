class Node:
    def __init__(self,key,val):
        self.key,self.val = key,val
        self.prev = self.next = None
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = {}

        #left=lRU and  Right = Most recent
        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    #remove from LL
    def remove(self,node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev
        
    #Insert node at right
    def insert(self,node):
        prev, nxt = self.right.prev, self.right
        node.prev, node.next = prev, nxt
        prev.next = nxt.prev = node
        node.prev, node.next = prev, nxt

    def get(self,key):
        if key in self.cache:
            #TODO is that update most recent
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
        
    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
         
        if len(self.cache) > self.cap:
            lru = self.left.next
            self.remove(lru) 
            del self.cache[lru.key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
