# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        lst2 = slow.next
        slow.next = None
        

        
        prev = None
        while lst2:
            tem = lst2.next
            lst2.next = prev
            prev = lst2
            lst2 = tem

        c1, c2 = head, prev
        while c2:
            tem1, tem2 = c1.next, c2.next
            c1.next = c2
            c2.next = tem1
            c1 = tem1
            c2 = tem2
        
            