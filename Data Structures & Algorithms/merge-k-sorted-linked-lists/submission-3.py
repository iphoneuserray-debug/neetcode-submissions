# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def conquer(self, list1, list2):
        dummy = ListNode(0, None)
        curr = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        if list1:
            curr.next = list1
        else:
            curr.next = list2
        return dummy.next


    def devide(self, lists, l, r):

        if l > r:
            return None
        if l == r:
            return lists[l]

        mid = l + (r - l) // 2
        left = self.devide(lists, l, mid)
        right = self.devide(lists, mid + 1, r)

        return self.conquer(left, right)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        i = 1
        n = len(lists)
        if n == 0:
            return None
        if n == 1:
            return lists[0]
        return self.devide(lists, 0, n - 1)
            