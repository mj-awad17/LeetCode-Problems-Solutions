class Solution(object):
    def appendCharacters(self, s, t):
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                j+=1
            i+=1
        return len(t)-j