from LinkedList import LinkedList

def reverse(head):
    prev, next = None, None
    curr = head
    
    while curr is not None:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        
    head = prev
    return head


print("Test Case 1: [1,2,3,4,5]")
ll1 = LinkedList([1, 2, 3, 4, 5])
print(f"Original: {ll1}")

# Reverse the linked list
ll1.head = reverse(ll1.head)
print(f"Reversed: {ll1}")
print("Expected: [5, 4, 3, 2, 1]\n")