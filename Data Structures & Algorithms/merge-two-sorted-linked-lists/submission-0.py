# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1 = list1
        l2 = list2
        head = ListNode()
        x = head
        while l1 and l2:
            if l1.val <= l2.val:
                x.next = l1
                l1 = l1.next
            else:
                x.next = l2
                l2 = l2.next
            x = x.next
        if l1 is None:
            x.next = l2
        else:
            x.next = l1
        return head.next
        