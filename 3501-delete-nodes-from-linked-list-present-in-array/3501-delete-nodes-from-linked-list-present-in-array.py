# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        # storing all nums in set()
        num_set = set(nums)

        # initlize head and new dummy node for handle edge case
        dummy = ListNode(0)
        dummy.next = head

        # two pointers
        prev, current = dummy, head

        while current:
            if current.val in num_set:
                # skip current node by linking prev to current.next
                prev.next = current.next
            else:
                # move prev to current if current is not removed
                prev = current
            # move to next node in the list
            current = current.next
        # return new head (which is dummy.next)
        return dummy.next