<h1><a href="https://leetcode.com/problems/combinations">combinations</a></h1>

<img src='https://img.shields.io/badge/Difficulty-Medium-orange' alt='Difficulty: Medium' />
<hr>
<p>
Given two integers <code>n</code> and <code>k</code>, return all possible combinations of <code>k</code> numbers chosen from the range <code>[1, n]</code>.
<br>
You may return the answer in <strong>any order</strong>.
</p>
<p><strong>Example 1:</strong></p>

        Input: n = 4, k = 2
        Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
        Explanation: There are 4 choose 2 = 6 total combinations.
        Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

<p><strong>Example 2:</strong></p>
        
        Input: n = 1, k = 1
        Output: [[1]]
        Explanation: There is 1 choose 1 = 1 total combination.
        
<p><strong>Constraints:</strong></p>

<ul>
<li><code>1 <= n <= 20</code></li>
<li><code>1 <= k <= n</code></li>
</ul>
