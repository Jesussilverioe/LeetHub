# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        cl1,cl2 = l1,l2
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        
        while cl1 or cl2 or carry:
            val1 = cl1.val if cl1 else 0
            val2 = cl2.val if cl2 else 0 
            total = val1+val2+carry
            carry = total//10
            total = total%10
            
            cur.next = ListNode(total)
            
            cur = cur.next
            cl1 = cl1.next if cl1 else None
            cl2 = cl2.next if cl2 else None
            
        return dummy.next