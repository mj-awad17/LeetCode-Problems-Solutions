class Solution(object):
    def reverseString(self, s):
        # two pointers
        left, right = 0, len(s) - 1

        # loop untill match condition
        while left < right:
            # swap the elements
            s[left], s[right] = s[right], s[left]
            # move the pointers
            left += 1
            right -= 1