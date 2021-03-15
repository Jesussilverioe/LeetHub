# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        slow = head
        mydic = {}
        while slow:
            if slow in mydic:
                return slow
            mydic[slow] = slow
            slow = slow.next
            
        if not slow:
            return None