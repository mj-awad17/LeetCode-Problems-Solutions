# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # Basic conditions
        if list1 == None and list2 == None:
            return None
        elif list1 != None and list2 == None:
            return list1
        elif list2 != None and list1 == None:
            return list2
        else:
            # dummy Node for merging the list1 and list2
            dummy = ListNode()
            tail = dummy
            while list1 and list2:
                if list1.val < list2.val:
                    # connet the list1 val-1 to dummy node
                    tail.next = list1
                    # update list1
                    list1 = list1.next
                else:
                    tail.next = list2
                    list2 = list2.next
                # update tail
                tail = tail.next

            if list1:
                tail.next = list1
            else:
                tail.next = list2


        return dummy.next