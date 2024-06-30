class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # two pointer
        i, j = 0, 0
        # iterate arrays
        while (i < len(s) and j < len(t)):
            # s ith elemnet equal to t jth element
            if s[i] == t[j]:
                # move i
                i += 1
            # move j
            j += 1
        if i == len(s):
            return True
        return False
        # return True if i == len(s) else False