# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        cur = head
        prev = None
        my_dic = {val:1}
        while cur:
            if cur.val in my_dic:
                if cur is head:
                    head = cur.next
                    cur = head
                    continue
                prev.next = cur.next
                cur = None
            else:
                prev = cur
            cur = prev.next 
        return head