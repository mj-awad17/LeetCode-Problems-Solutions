<h2><a href="https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/">Remove All Adjacent Duplicates In String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>

<p>
You are given a string <code>s</code> consisting of lowercase English letters. A <b>duplicate removal</b> consists of choosing two <b>adjacent</b> and <b>equal</b> letters and removing them.

We repeatedly make <b>duplicate removals</b> on <code>s</code> until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is <b>unique</b>.
</p>

<p><strong>Example 1:</strong></p>

    Input: s = "abbaca"
    Output: "ca"
    Explanation: 
    For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".

<p><strong>Example 2:</strong></p>

    Input: s = "azxxzy"
    Output: "ay"


<p><strong>Constraints:</strong></p>


<ul>
    <li><code>1 <= s.length <= 105</code></li>
    <li><code>s consists of lowercase English letters.</code></li>
</ul>
