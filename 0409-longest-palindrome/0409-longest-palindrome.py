class Solution(object):
    def longestPalindrome(self, s):
        # Count the frequency of each character
        char_freq = {}
        for char in s:
            char_freq[char] = char_freq.get(char, 0) + 1
        
        # Compute the length of the longest palindrome
        length = 0
        has_odd = False
        for count in char_freq.values():
            length += count // 2 * 2
            if count % 2 == 1:
                has_odd = True
        
        # If there is at least one character with an odd frequency, add 1 to the length
        if has_odd:
            length += 1
        
        return length