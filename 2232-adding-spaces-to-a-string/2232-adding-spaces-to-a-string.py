class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        result = []
        space_index = 0
        n = len(spaces)

        for i in range(len(s)):
            if space_index < n and i == spaces[space_index]:
                result.append(' ')  # Add space before the character
                space_index += 1
            result.append(s[i])  # Add the character

        return ''.join(result)    
    """m, n=len(spaces), len(s)
        spaces.append(n)
        
        t=[' ']*(m+n)
        i, j=0, 0
        while i<n:
            while i<n and i!=spaces[j]:
                t[i+j]=s[i]
                i+=1
            if j<m:
                t[i+j+1]=s[i]
                j+=1
            i+=1
        return "".join(t)"""
        