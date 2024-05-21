<h2><a href="https://leetcode.com/problems/find-the-integer-added-to-array-i/"></a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>
You are given two arrays of equal length, <code>nums1</code> and <code>nums2</code>
Each element in <code>nums1</code> has been increased (or decreased in the case of negative) by an integer, represented by the variable <code>x</code>.
<br>
As a result, <code>nums1</code> becomes <strong>equal</strong> to <code>nums2</code>. Two arrays are considered <strong>equal</strong> when they contain the same integers with the same frequencies.
<br>
Return the integer <code>x</code>.
</p>

<p><strong>Example 1:</strong></p>

    Input: nums1 = [2,6,4], nums2 = [9,7,5]

    Output: 3

    Explanation:

    The integer added to each element of nums1 is 3.

<p><strong>Example 2:</strong></p>

    Input: nums1 = [10], nums2 = [5]

    Output: -5

    Explanation:

    The integer added to each element of nums1 is -5.


<p><strong>Example 3:</strong></p>

    Input: nums1 = [1,1,1,1], nums2 = [1,1,1,1]

    Output: 0

    Explanation:

    The integer added to each element of nums1 is 0.

<p><strong>Constraints:</strong></p>
<ul>
<li><code>1 <= nums1.length == nums2.length <= 100</code></li>
<li><code>0 <= nums1[i], nums2[i] <= 1000</code></li>
<li>The test cases are generated in a way that there is an integer <code>x</code> such that <code>nums1<code> can become equal to <code>nums2<code> by adding <code>x</code> to each element of <code>nums1</code>.</li>
</ul>