class Solution:
    def validPalindrome(self, s: str) -> bool:
        #[::-1]
        l = 0 
        r = len (s) - 1
        while l < r : 
            if s[l] == s[r]:
                l +=1
                r -=1
            else:
                return s[l:r] == s[l:r][::-1] or s[l+1:r+1] == s[l+1:r+1][::-1]
        return True
        '''
        time : O(n)
        space : O(1)
        '''