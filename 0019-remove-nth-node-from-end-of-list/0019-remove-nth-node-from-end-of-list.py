# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # start with dummy node to take help
        dummy = ListNode(0, head)
        # pointer
        slow = fast = dummy
        # loop to check next node ahead
        for _ in range(n+1):
            fast = fast.next
        
        # move pointer to end
        while fast:
            fast = fast.next
            slow = slow.next
        
        # removeing the node
        slow.next = slow.next.next
        return dummy.next