# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or head.next == None:
            return head
        cur = head
        count = 0
        while cur:
            count += 1
            cur = cur.next
        
        rotate_count = k%count
        cur = head
        for _ in range(rotate_count):
            while cur.next:
                prev = cur
                cur = cur.next
            prev.next = None
            cur.next = head
            head = cur
            
        return head

        