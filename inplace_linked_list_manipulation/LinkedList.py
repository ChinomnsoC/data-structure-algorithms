class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, values=None):
        self.head = None
        
        # If values provided, create the linked list
        if values:
            for value in values:
                self.append(value)
    
    def append(self, data):
        """Add a new node at the end"""
        new_node = ListNode(data)
        
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
    
    def __str__(self):
        """Return string representation like [2,1,4,3,5]"""
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return str(result)

# Example usage:
if __name__ == "__main__":
    # Create a linked list from a regular list
    ll = LinkedList([2, 1, 4, 3, 5])
    print(ll)  # Output: [2, 1, 4, 3, 5]
    
    # Create empty and add elements
    ll2 = LinkedList()
    ll2.append(10)
    ll2.append(20)
    print(ll2)  # Output: [10, 20]