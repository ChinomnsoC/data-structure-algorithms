# Given an array of integers, return the indices of the two numbers that add up to a target sum.

def two_sum(nums: list, target: int) -> list:
    num_to_index = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in num_to_index:
            return [num_to_index[complement], i]
        
        num_to_index[num] = i

    
    return []

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: ListNode) -> bool:
    visited = set()
    
    while head is not None:
        if head in visited:
            return True
        
        visited.add(head)
        
        head = head.next
    return False


def do_tests_pass() -> bool:
    assert two_sum([2, 7, 11, 15], 9) == [0, 1]
    assert two_sum([3, 2, 4], 6) == [1, 2]
    assert two_sum([3, 3], 6) == [0, 1]

    return True

def do_cycle_tests_pass() -> bool:
        # Cycle example
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2  # cycle back to node2

    assert has_cycle(node1) == True
    

    # No cycle example
    nodeA = ListNode(1)
    nodeB = ListNode(2)
    nodeC = ListNode(3)
    nodeA.next = nodeB
    nodeB.next = nodeC
    # nodeC.next = None (no cycle)
    assert has_cycle(nodeA) == False
    
    return True

if __name__ == "__main__":
    if do_tests_pass() and do_cycle_tests_pass():
        print("All tests pass")
    else:
        print("Tests fail")





# **Examples:**
# ```
# 1 -> 2 -> 3 -> 4 -> 2 (cycle back to node 2) → True
# 1 -> 2 -> 3 → False