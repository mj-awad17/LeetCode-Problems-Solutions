# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # # base case
        if not head.next:
            return None
        # two pointers
        s = head
        f= head.next.next
        # end of the list through f pointer
        while f and f.next:
            s = s.next
            f = f.next.next
        s.next = s.next.next
        return head