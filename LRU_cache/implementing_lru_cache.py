# Definition for a Linked List node
class LinkedListNode:
    def __init__(self, pair):
        self.second = pair[1]
        self.first = pair[0]
        self.pair = pair
        self.next = None
        self.prev = None

# We will use a linkedlist of a pair of integers
# where the first integer will be the key
# and the second integer will be the value

class LRUCache:
    def __init__(self, capacity):
        # Write your code here
        # capacity, head, tail, prev, next, cache
        self.capacity = capacity
        self.head = LinkedListNode([-1, -1])
        self.tail = LinkedListNode([-1, -1])
        self.cache = {}
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        # Replace this placeholder return statement with your code
        # if the key is not in cache, return -1
        # else, return value, then move the key value pair to head in the cache
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self._remove_node(node)
            self._set_node_as_head(node)
            return node.second
            
    def _remove_node(self, node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
    
    # [head, 2, 5, 8, 9, tail]
    def _set_node_as_head(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        
        

    def set(self, key, value):
        # Write your code here
        # if the key exists, update its value to the new value
        if key in self.cache:
            node = self.cache[key]
            node.second = value
            node.pair = [key, value]
            
            # then move key value pair to the head.
            self._remove_node(node)
            self._set_node_as_head(node)
            return
        # if it doesn't exist, and cache at capacity, delete tail,
        # [head, 2, 5, 8, 9, tail]
        if len(self.cache) >= self.capacity:
            lru_node = self.tail.prev
            self._remove_node(lru_node)
            del self.cache[lru_node.first]
        
        # if it doesn't exist and we are not at capacity
        # create new node with key value pair
        new_node = LinkedListNode([key, value])
        
        # add key value to LRUCache
        self.cache[key] = new_node
        
        # update linked list with new node at head
        self._set_node_as_head(new_node)
