from LinkedList import LinkedList



def reorder_list(head):
    if not head:
        return head
    
    # Finding the middle
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    prev, curr = None, slow
    
    # here we say when current is the middle, we reverse from the middle
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    # then we set the head to be the first, and the second to be the last  
    first, second = head, prev

    while second.next:
        first.next, first = second, first.next
        second.next, second = first, second.next
    
    
    return head


print("Test Case 1: [9,1,2,4,8,6]")
ll1 = LinkedList([9, 1, 2, 4, 8, 6])
print(f"Original: {ll1}")

ll1.head = reorder_list(ll1.head)
print(f"Reversed: {ll1}")
print("Expected: [9, 5, 1, 4, 2, 3]\n")