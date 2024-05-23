"""
Intuition:
This approach uses the itertools.combinations() function from the standard library, which is a more concise and efficient way to generate all possible combinations.
The range(1, n+1) generates a sequence of numbers from 1 to n, and itertools.combinations() generates all possible combinations of size k from this sequence.
Complexity:
The time complexity is the same as the previous approach: O(n choose k).
The space complexity is also O(n), as the function creates a list of size n to store the numbers from 1 to n.
"""
class Solution(object):
    def combine(self, n, k):
        return list(itertools.combinations(range(1, n+1), k))