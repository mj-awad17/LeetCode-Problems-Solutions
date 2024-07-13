# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        def reverseLL(head):
            if not head or not head.next:
                return head
            
            # reverse the current node
            last = reverseLL(head.next)
            head.next.next = head
            head.next = None
            
            return last
        # finding middle using two pointers
        slow, fast = head, head
        while (fast and fast.next):
            slow = slow.next
            fast = fast.next.next

        rev = reverseLL(slow)
        curr = head
        while(rev.next != None):
            # store next nodes
            tempCurr = curr.next
            curr.next = rev
            
            # merge nodes
            tempRev = rev.next
            rev.next = tempCurr

            # move to next node
            curr = tempCurr
            rev = tempRev