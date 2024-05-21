"""
# 2 - Bit Manipulation Approach

**Intuition:**

The intuition behind this solution is to use the fact that the number of subsets of a set with `n` elements is `2^n`. We can represent each subset as a binary number, where each bit represents the presence or absence of an element in the subset.

**Approach:**

The approach can be summarized as follows:

1. Initialize an empty `result` list to store the generated subsets.
2. Determine the length of the `nums` array and store it in the variable `n`.
3. Iterate through all possible binary numbers from `0` to `2^n - 1` using a `for` loop.
4. For each binary number `mask`, create a new empty subset `subset`.
5. Iterate through each index `i` in the range `[0, n)`.
6. Check if the `i`-th bit of `mask` is set (i.e., `mask & (1 << i)` is non-zero). If it is, append the corresponding element `nums[i]` to the `subset`.
7. After processing all the bits, append the `subset` to the `result` list.
8. Return the `result` list, which contains all the generated subsets.

The key idea behind this approach is that each binary number from `0` to `2^n - 1` represents a unique subset, where the presence or absence of an element in the subset is determined by the value of the corresponding bit in the binary number.

**Complexity Analysis:**

- **Time Complexity:** O(N * 2^N), where N is the length of the `nums` array. This is because we iterate through all possible binary numbers from `0` to `2^n - 1`, which takes O(2^N) time. For each binary number, we need to iterate through the `n` bits, which takes O(N) time.
- **Space Complexity:** O(N * 2^N), as we need to store all 2^N possible subsets, each of which can have a maximum length of N.

"""
class Solution(object):
    def subsets(self, nums):
        result = []
        n = len(nums)
        for mask in range(2 ** n):
            subset = []
            for i in range(n):
                if mask & (1 << i):
                    subset.append(nums[i])
            result.append(subset)
        return result