<h1><a href="https://leetcode.com/problems/merge-strings-alternately/">Merge-String-Alternatively
</a></h1>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy' />
<hr>
<p>
  You are given two strings <code>word1</code>code> and <code>word2</code>code>. Merge the strings by adding letters in alternating order, starting with <code>word1</code>code>. If a string is longer than the other, append the additional letters onto the end of the merged string.
<br>
Return the merged string.
</p>

<h3>Example 1</h3>
<pre><strong>Input: </strong> word1 = "abc", word2 = "pqr"
<strong>Output: </strong> "apbqcr"
<strong>Explaination: </strong> The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
</pre>

<h3>Example 2</h3>
<pre><strong>Input: </strong> word1 = "ab", word2 = "pqrs"
<strong>Output: </strong> "apbqrs"
<strong>Explaination: </strong> Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
</pre>

<h3>Example 3</h3>
<pre><strong>Input: </strong> word1 = "abcd", word2 = "pq"
<strong>Output: </strong> "apbqcd"
<strong>Explaination: </strong> Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
</pre>

<h3>Constraints:</h3>
<ul>
<li><code>1 <= word1.length, word2.length <= 100</code></li>
<li><code>word1</code> and <code>word2</code> consist of lowercase English letters..</li>

</ul>
