"""
Intuition: 

The basic idea is the same as the previous approach, but we use memoization to store the results of subproblems to avoid redundant computations.

Approach:

1. Define a helper function backtrack that takes the starting index start as a parameter.
2. If start reaches the end of the string, return a list containing an empty list, as we have found a valid partition.
3. Check if the current start index is already in the memoization dictionary memo. If so, return the stored result. Otherwise, initialize an empty list partitions to store the valid partitions.
4. Iterate through the possible ending indices end starting from start.
5. Check if the substring s[start:end+1] is a palindrome. If it is, recursively call backtrack with the next starting index end+1 and append the current palindrome substring to the right partitions.
6. Store the current partitions in the memo dictionary with the key start, and return the partitions.
7. In the main partition function, call the backtrack function with the initial starting index 0 and return the result.

Complexity:
Time Complexity: O(N * 2^N), where N is the length of the input string. The memoization reduces the number of redundant computations, but the overall time complexity remains the same as the previous approach.

Space Complexity: O(N * 2^N), where N is the length of the input string. This is due to the memoization and the storage of all the possible partitions.
"""
class Solution(object):
    def partition(self, s):
        memo = {}

        def backtrack(start):
            if start == len(s):
                return [[]]

            if start in memo:
                return memo[start]

            partitions = []
            for end in range(start, len(s)):
                if s[start:end+1] == s[start:end+1][::-1]:
                    for right in backtrack(end+1):
                        partitions.append([s[start:end+1]] + right)

            memo[start] = partitions
            return partitions

        return backtrack(0)