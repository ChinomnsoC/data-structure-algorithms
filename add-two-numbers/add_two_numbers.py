from typing import Optional, ListNode

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# class Solution:
#     def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

class Solution:
    def addTwoNumbers(self, l1, l2):
        def convert_to_int(node):
            result = 0
            while node:
                result = result * 10 + node.val
                node = node.next
            return result

        num1 = convert_to_int(l1)
        num2 = convert_to_int(l2)
        total = num1 + num2

        # create a dummy head node
        dummy_head = ListNode()
        current = dummy_head
    
        # change the total back to a reverse linked list 
        for digit in reversed(str(total)):
            current.next = ListNode(int(digit))
            current = current.next
    
        return dummy_head.next