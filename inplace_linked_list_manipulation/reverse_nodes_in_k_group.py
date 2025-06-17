from LinkedList import LinkedList, ListNode


def reverse_k_groups(head, k):
    dummy = ListNode(0)
    dummy.next = head
    pointer = dummy
    
    while pointer != None:
        
        tracker = pointer
        
        print("\t\tptr:", pointer.data)
        for i in range(k):
            if tracker == None:
                break
            
            tracker = tracker.next
            print(tracker.data, end = " ") if tracker else print("", end = "")
        if tracker == None:
            break
        prev, curr = reverse(pointer.next, k)
        last_node_of_reversed_group = pointer.next
        last_node_of_reversed_group.next = curr
        pointer.next = prev
        pointer = last_node_of_reversed_group

    return dummy.next
def reverse(head, k):
    prev, curr, next = None, head, None

    for _ in range(k):
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    return prev, curr


print("Test Case 1: [1,2,3,4,5]")
ll1 = LinkedList([1, 2, 3, 4, 5])
print(f"Original: {ll1}")

# Reverse the linked list
ll1.head = reverse_k_groups(ll1.head, 2)
print(f"Reversed: {ll1}")
print("Expected: [2, 1, 4, 3, 5]\n")