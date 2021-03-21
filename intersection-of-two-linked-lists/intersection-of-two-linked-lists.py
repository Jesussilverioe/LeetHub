# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        cur1 = headA
        cur2 = headB
        
        if not cur1 or not cur2:
            return None
        
        lendif = 0
        while cur1.next:
            lendif += 1
            cur1 = cur1.next
        while cur2.next:
            lendif -= 1
            cur2 = cur2.next
            
        if cur1 != cur2:
            return None
        
        cur1 = headA
        cur2 = headB
        
        while lendif != 0:
            if lendif > 0:
                cur1 = cur1.next
                lendif -= 1
            else:
                cur2 = cur2.next
                lendif += 1
        
        while cur1 != cur2:
            cur1 = cur1.next
            cur2 = cur2.next
        return cur1
        
        
        
        