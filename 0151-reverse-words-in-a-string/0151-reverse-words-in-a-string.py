class Solution(object):
    def reverseWords(self, s):
        words = s.split()
        reverse_s = ' '.join(words[::-1])
        return reverse_s