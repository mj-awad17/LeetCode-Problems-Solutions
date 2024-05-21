"""
# 1- Iterative Approach

**Intuition:**

The intuition behind this solution is to use an iterative approach to generate all possible subsets of the given array `nums`. The idea is to start with an empty set and then iteratively add each element from the `nums` array to the existing subsets, creating new subsets in the process.

**Approach:**

The approach can be summarized as follows:

1. Initialize the `result` list with an empty subset `[[]]`. This represents the base case, where the empty set is a subset of any set.
2. Iterate through each element `num` in the `nums` array.
3. For each `num`, create new subsets by adding `num` to each of the existing subsets in the `result` list.
4. Append the new subsets to the `result` list.
5. Repeat steps 2-4 until all elements in `nums` have been processed.
6. Return the final `result` list containing all the generated subsets.

This approach ensures that all possible subsets are generated, and no duplicate subsets are included in the final result.

**Complexity Analysis:**

- **Time Complexity:** O(N * 2^N), where N is the length of the `nums` array. This is because for each element in `nums`, we create 2^(i-1) new subsets, where `i` is the index of the current element. In total, there are 2^N possible subsets, and for each one, we need to create a new list, which takes O(N) time.
- **Space Complexity:** O(N * 2^N), as we need to store all 2^N possible subsets, each of which can have a maximum length of N.

"""
class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for num in nums:
            result += [subset + [num] for subset in result]
        return result
        