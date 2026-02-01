class Node:
    def __init__(self, key, value):
        self.prev = None
        self.next = None
        self.key = key
        self.value = value
        

class LRUCache:
    def __init__(self, capacity):
        # initialise lru cache
        # cache, capacity, set head, set tail, link the head and the tail
        self.cache = {}
        self.capacity = capacity
        
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        
        # [head, tail]
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def get(self, key):
        # if key not in cache, return -1
        if key not in self.cache:
            return -1
        
        else:
            node = self.cache[key]
            
            self._remove_node(node)
            self._set_node_as_head(node)
            return node.value
        # else, return the value of the node.
        # but before you return, update the node in the linked list to be at the head. 
    
          # 9
    # [head, 3, 5, 8 tail]
    
    def _remove_node(self, node):
        prev_node = node.prev #5
        next_node = node.next # 8
        prev_node.next = next_node
        next_node.prev = prev_node
        
    def _set_node_as_head(self, node):
        head_node = self.head.next
        # 9's prev should be head
        node.prev = self.head
        # 9's next should be head's next
        node.next = head_node
        
        # head's next's prev should be 9
        self.head.next.prev = node
        
        # head's next should be 9
        self.head.next = node
        
    def put(self, key, value):
        # if the key is in cache, update the value with new value in cache,
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            
            self._remove_node(node)
            self._set_node_as_head(node)
            
            return
        
        # else if we are at capacity
        # delete tail in linked list
        # delete key value pair from cache hashmap
        if len(self.cache) >= self.capacity:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.cache[lru_node.key]
        
        
        
        # else if we are not at capacity
        # make a new node
        new_node = Node(key, value)
        
        # update linked list with new node
        self._set_node_as_head(new_node)
        
        # update cache with new key value pair
        self.cache[new_node] = new_node.value
        