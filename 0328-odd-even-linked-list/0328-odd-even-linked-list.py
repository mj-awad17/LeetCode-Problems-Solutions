# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # list is empty or has only one node
        if ((head == None) or (head.next == None)):
            return head
        # Initialize pointers
        even = head.next
        odd = head
        evenHead = even
        # reach the end of the list
        while((even != None) and (even.next != None)):
            # Connect the current node to the next node
            odd.next = odd.next.next
            even.next = even.next.next
            # move the pointers forward
            odd = odd.next
            even = even.next
        # link the end of the odd list to the head of the even list
        odd.next = evenHead
        return head