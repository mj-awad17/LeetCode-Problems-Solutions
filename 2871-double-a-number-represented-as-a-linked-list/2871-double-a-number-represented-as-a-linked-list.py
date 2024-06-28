class Solution(object):
    def doubleIt(self, head):
        # Convert linked list to integer
        num = 0
        curr = head
        while curr:
            num = num * 10 + curr.val
            curr = curr.next
        
        # Double the integer
        num *= 2
        
        # Convert integer back to linked list
        dummy = ListNode(0)
        curr = dummy
        for char in str(num):
            curr.next = ListNode(int(char))
            curr = curr.next
        
        return dummy.next