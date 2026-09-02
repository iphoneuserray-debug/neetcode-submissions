# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head
        curr_f = head
        while curr_f and curr_f.next:
            curr = curr.next
            curr_f = curr_f.next.next
            if curr == curr_f:
                return True
        return False