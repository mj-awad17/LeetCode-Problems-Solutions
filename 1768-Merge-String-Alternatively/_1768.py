"""
Approach - 1

Intuition:
The intuition behind this solution is to merge the two input strings `word1` and `word2` in an alternating fashion. 
We start by initializing an empty string `res` to store the merged result. Then, we iterate through the maximum length of 
the two input strings, and for each index `i`, we append the character at index `i` from `word1` and `word2` to the `res` string.

Approach:
The approach used in this solution is also a **Greedy** approach, similar to the previous solution. We iterate through the two
input strings simultaneously, adding characters to the `res` string in an alternating fashion.

Complexity:
- **Time Complexity:** O(max(n, m)), where n and m are the lengths of `word1` and `word2`, respectively. 
- **Space Complexity:** O(n + m), where n and m are the lengths of `word1` and `word2`, respectively. 
"""
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
      # empty result string
        res = ""
      # loop to iterate the word1 and word2 lengths
        for i in range(max(len(word1), len(word2))):
            if i < len(word1):
                res += word1[i]
            if i < len(word2):
                res += word2[i]
        return res

"""
Approach - 2

Intuition:
The intuition behind this solution is to merge the two input strings `word1` and `word2` in an alternating fashion.
We start by iterating through the two strings simultaneously, appending characters from `word1` and `word2` to the `res` list in an alternating manner.
Once we reach the end of one of the strings, we append the remaining characters from the other string to the `res` list.

Approach:
The approach used in this solution is a **Greedy** approach. 
We iterate through the two input strings simultaneously, adding characters to the `res` list in an alternating fashion. 
This allows us to merge the two strings in the desired manner.

Complexity:
- **Time Complexity:** O(max(n, m)), where n and m are the lengths of `word1` and `word2`, respectively. 
- **Space Complexity:** O(n + m), where n and m are the lengths of `word1` and `word2`, respectively.
"""
class Solution(object):
    def mergeAlternately(self, word1, word2):
        i,j = 0,0
        res = []
        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i +=1
            j +=1
        res.append(word1[i:])
        res.append(word2[j:])
        return "".join(res)
