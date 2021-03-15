# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        prev = None
        slow = head
        fast = head
        
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next
            
        prev.next = None
        return self.merged(self.sortList(head), self.sortList(slow))
    
    def merged(self, l1, l2):
        dummy = ListNode('dummy')
        cur = dummy
        while l1 and l2:
            if l2.val < l1.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
                
        if l2:
            cur.next = l2
        else:
            cur.next = l1
        return dummy.next
        