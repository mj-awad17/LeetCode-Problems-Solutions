class Solution(object):
    def isAnagram(self, s, t):
        s_sort = sorted(s)        
        t_sort = sorted(t)
        if s_sort == t_sort:
            return True
        return False