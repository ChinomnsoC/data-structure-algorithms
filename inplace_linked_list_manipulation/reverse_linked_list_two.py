from LinkedList import LinkedList, ListNode


def reverse_between(head, left, right):
    if not head or left == right:
        return head
    
    dummy = ListNode(0)
    dummy.next = head
    prev = dummy
    
    # Move prev to the node just before the left position
    for _ in range(left - 1):
        prev = prev.next

    # Current node is the node at left position
    curr = prev.next
    
    for _ in range(right - left):
        # next = curr.next
        # curr.next = prev
        # prev = curr
        # curr = next
        
        next_node = curr.next
        curr.next = next_node.next
        next_node.next = prev.next
        prev.next = next_node
        
        
    return dummy.next


print("Test Case 1: [1,2,3,4,5]")
ll1 = LinkedList([1, 2, 3, 4, 5])
print(f"Original: {ll1}")

# Reverse the linked list
ll1.head = reverse_between(ll1.head, 2, 4)
print(f"Reversed: {ll1}")
print("Expected: [1, 4, 3, 2, 5]\n")