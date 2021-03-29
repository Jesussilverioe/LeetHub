# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        cur_list1 = l1
        cur_list2 = l2
        
        merged_cur = None
        new_head = None
        
        if not cur_list1:
            return l2
        if not cur_list2:
            return l1
        
        if cur_list1.val <= cur_list2.val:
            merged_cur = cur_list1
            cur_list1 = cur_list1.next
        else:
            merged_cur = cur_list2
            cur_list2 = cur_list2.next
        
        new_head = merged_cur
        
        while cur_list1 and cur_list2:
            if cur_list1.val < cur_list2.val:
                merged_cur.next = cur_list1
                merged_cur = merged_cur.next
                cur_list1 = cur_list1.next
            else:
                merged_cur.next = cur_list2
                merged_cur = merged_cur.next
                cur_list2 = cur_list2.next
                
        if not cur_list1:
            merged_cur.next = cur_list2
        if not cur_list2:
            merged_cur.next = cur_list1
            
        return new_head