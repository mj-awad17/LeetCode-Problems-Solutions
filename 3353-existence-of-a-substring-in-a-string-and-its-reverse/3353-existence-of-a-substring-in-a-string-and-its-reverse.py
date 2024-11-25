class Solution:
    def isSubstringPresent(self, s: str) -> bool:
        # reverse the string
        rev = s[::-1]
        l = len(s)
        i = 0
        
        # iterate throught the lenght
        while i < l-1:
            if s[i:i+2] in rev:
                return True
            i += 1
        
        return False