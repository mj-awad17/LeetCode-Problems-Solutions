class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, maxlen = 0, 0
        sett = set()

        for right in range(len(s)):
            while s[right] in sett:
                sett.remove(s[left])
                left += 1
            sett.add(s[right])
            maxlen = max(maxlen, right - left + 1)
        return maxlen