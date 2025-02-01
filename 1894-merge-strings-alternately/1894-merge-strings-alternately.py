class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        # inilization 
        res = []
        i, j = 0, 0

        # iteration loop
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1

        # remaining elements from the words
        res.append(word1[i:])
        res.append(word2[j:])

        # result 
        return "".join(res)