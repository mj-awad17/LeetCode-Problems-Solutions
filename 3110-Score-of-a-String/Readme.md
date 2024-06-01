<h2><a href="https://leetcode.com/problems/score-of-a-string/">Score of a String</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy'/>
<hr>
<p>
  You are given a string <code>s</code>. The <strong>score</strong> of a string is defined as the sum of the absolute difference between the <strong>ASCII</strong> values of adjacent characters.
<br/>
Return the score of <code>s</code>.
</p>

<h3>Example 1</h3>
<pre><strong>Input: </strong> s = "hello"
<strong>Output: </strong> 13
<strong>Explaination: </strong> The <strong>ASCII</strong> values of the characters in <code>s</code> are: <code>'h' = 104</code>, <code>'e' = 101</code>, <code>'l' = 108</code>, <code>'o' = 111</code>. So, <br>the score of <code>s</code> would be <code>|104 - 101| + |101 - 108| + |108 - 108| + |108 - 111| = 3 + 7 + 0 + 3 = 13</code>.
</pre>

<h3>Example 2</h3>
<pre><strong>Input: </strong>  s = "zaz"
<strong>Output: </strong> 50
<strong>Explaination: </strong> The <strong>ASCII</strong> values of the characters in <code>s</code> are: <code>'z' = 122</code>, <code>'a' = 97</code>. So, <br>the score of <code>s</code> would be <code>|122 - 97| + |97 - 122| = 25 + 25 = 50</code>.
</pre>

<h3>Constraints:</h3>
<ul>
<li><code>2 <= s.length <= 100</code></li>
<li><code>s</code>consists only of lowercase English letters.</li>

</ul>
