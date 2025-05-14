# Define the Node class for the singly linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return str(self.value)


# Helper function to print the entire linked list
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


# Function to remove the nth node from the end of the list
def remove_nth_last_node(head, n):
    print(f"\nRemoving {n}th node from the end...\n")

    # Step 1: Initialize two pointers to head
    right = head
    left = head
    print("Initial head of list:")
    print_list(head)

    # Step 2: Move the 'right' pointer n steps ahead
    for i in range(n):
        print(range(n))
        if right:
            print(f"Moving right pointer to step {i+1}: at node {right.value}")
            right = right.next

    # Step 3: If right is None after moving n steps, we are deleting the head
    if not right:
        print(
            f"After moving {n} steps, right is None. Removing head node {head.value}."
        )
        return head.next  # Remove the head node

    # Step 4: Move both pointers until right reaches the end
    while right.next:
        print(f"Right is at {right.value}, Left is at {left.value}")
        right = right.next
        left = left.next
        print(right, left)

    print(f"Node to be removed: {left.next.value}")

    # Step 5: Skip the target node
    left.next = left.next.next

    print("Updated list after deletion:")
    print_list(head)

    return head


# Helper function to create a linked list from a list of values
def create_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next


# --------------------------
# Example usage
# --------------------------

# Create a sample list: 1 -> 2 -> 3 -> 4 -> 5
head = create_linked_list([3, 4, 8, 23, 5, 88, 9, 45])

# Call function to remove 2nd node from the end (which is 4)
updated_head = remove_nth_last_node(head, 9)

# Final output
print("\nFinal linked list:")
print_list(updated_head)
