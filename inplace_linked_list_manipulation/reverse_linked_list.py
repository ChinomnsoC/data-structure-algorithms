# Definition for a Linked List node
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from LinkedList import ListNode
# from ds_v1.LinkedList.LinkedList import ListNode

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