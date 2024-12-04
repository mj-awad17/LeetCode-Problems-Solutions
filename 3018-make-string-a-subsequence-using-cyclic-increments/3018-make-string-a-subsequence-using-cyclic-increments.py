class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        idx, n = 0, len(str2)

        for ch in str1:
            
            if idx == n:
                break
            # characters match, move to the next character in str2
            if ch == str2[idx]:
                idx += 1
                continue
            # Check if the next character (cyclic increment) matches
            next_ch = 'a' if ch == 'z' else chr(ord(ch)+1)
            if next_ch == str2[idx]:
                idx += 1
        
        return idx == n
        