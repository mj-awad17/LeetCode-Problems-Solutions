<h2><a href="https://leetcode.com/problems/sign-of-the-product-of-an-array/">Sign of the Product of an Array</a></h2>
<img src='https://img.shields.io/badge/Difficulty-Easy-green' alt='Difficulty: Easy'/>
<hr>
<p>
There is a function <code>signFunc(x)</code> that returns:
  <ul>
    <li><code>1</code> if <code>x</code> is positive.</li>
    <li><code>0</code> if <code>x</code> is negative.</li>
    <li><code>0</code> if <code>x</code> is equal to 0.</li>
  </ul>
  You are given an integer array <code>nums</code>. Let <code>product</code> be the product of all values in the array <code>nums</code>.
  <br>
Return <code>signFunc(product)</code>.
</p>

<h3>Example 1</h3>
<pre><strong>Input: </strong> nums = [-1,-2,-3,-4,3,2,1]
<strong>Output: </strong> 1
<strong>Explaination: </strong> The product of all values in the array is 144, and signFunc(144) = 1
</pre>

<h3>Example 2</h3>
<pre><strong>Input: </strong> nums = [1,5,0,2,-3]
<strong>Output: </strong> 0
<strong>Explaination: </strong> The product of all values in the array is 0, and signFunc(0) = 0
</pre>

<h3>Example 3</h3>
<pre><strong>Input: </strong> nums = [-1,1,-1,1,-1]
<strong>Output: </strong> -1
<strong>Explaination: </strong> The product of all values in the array is -1, and signFunc(-1) = -1
</pre>

<h3>Constraints:</h3>
<ul>
<li><code>1 <= nums.length <= 1000</code></li>
<li><code>-100 <= nums[i] <= 100</code></li>

</ul>
