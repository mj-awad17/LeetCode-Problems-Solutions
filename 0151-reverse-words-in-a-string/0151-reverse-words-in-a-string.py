class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reverse_w = words[::-1]
        reverse_s = ' '.join(reverse_w)
        return reverse_s