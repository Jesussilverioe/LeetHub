# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        cur = head
        newval = None
        if not head:
            return None
        
        while cur:
            newval = cur.next
            while newval and newval.val == cur.val:
                newval = newval.next
            cur.next = newval
            cur = cur.next
                
        return head
                