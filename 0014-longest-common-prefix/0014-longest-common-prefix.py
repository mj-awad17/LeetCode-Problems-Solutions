class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """strs.sort()
        str1, str2 = strs[0], strs[-1]
        result = ""
        for i in range(min(len(str1), len(str2))):
            if str1[i] == str2[i]:
                # result = result + str1[i]
                result += str1[i]
            else:
                break
        return result"""


        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or s[i] != strs[0][i]:
                    return res
            res += strs[0][i]
        return res
        """
        if not strs:
            return ""
        # Find the shortest string in the array
        shortest = min(strs, key=len)
        # Iterate through the characters of the shortest string
        for i, char in enumerate(shortest):
            # Check if all other strings have the same character at this position
            for s in strs:
                if s[i] != char:
                    return shortest[:i]
        # If all strings have the same characters, return the shortest string
        return shortest"""