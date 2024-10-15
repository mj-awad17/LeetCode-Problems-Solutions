# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
    # Two pointers approach: slow and fast to find the middle of the list
    slow, fast = head, head
    prev = None
    
    # Reverse the first half of the linked list while using fast pointer to reach the end.
    while fast and fast.next:
        # Move the fast pointer two steps forward
        fast = fast.next.next
        # Reverse the first half of the list
        temp = slow.next  # Save the next node
        slow.next = prev  # Reverse the link
        prev = slow       # Move prev forward
        slow = temp       # Move slow pointer forward
    # Now, slow points to the start of the second half of the list
    # and prev points to the reversed first half of the list.
    res = 0  # To store the maximum pair sum
    # Second while loop: Compare the nodes from the reversed first half and the second half.
    while slow:
        # Calculate the twin sum and update the result with the maximum sum
        res = max(res, prev.val + slow.val)
        
        # Move both pointers forward
        prev = prev.next
        slow = slow.next
    
    # Return the maximum twin sum
    return res
