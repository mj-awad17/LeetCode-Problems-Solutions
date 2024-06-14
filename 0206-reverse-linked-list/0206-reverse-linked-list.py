# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # two pointer previous, current
        previous = None
        current = head
        
        while current:
            # Store the next node
            next_node = current.next
            # Reverse the pointer of the current node
            current.next = previous
            # Move the pointers one step forward
            previous = current
            current = next_node

        # The last node visited will be the new head of the reversed list
        return previous