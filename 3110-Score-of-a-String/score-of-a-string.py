"""
Intuition:

1. Initialization: The variable `socre` is initialized to 0, which will be used to store the total score.
2. Iteration: The `for` loop iterates through the string `s`, starting from the first character (index 0) and going up to the second-to-last character (index `len(s) - 1`).
This ensures that we compare each character with the next character in the string.
3. Calculation: Inside the loop, the code calculates the absolute difference between the ASCII values of the current character `s[i]` and the next character `s[i+1]` using the `ord` function.
The absolute difference is then added to the `socre` variable.
4. Return: After the loop, the final value of `socre` is returned as the score of the input string `s`.

Complexity

Time complexity: O(n).
Space complexity: O(1).
"""
socre = 0
for i in range(len(s)-1):
    socre += abs(ord(s[i])-ord(s[i+1]))
return socre

"""
one line code as:
"""
return sum(abs(ord(s[i])-ord(s[i+1])) for i in range(len(s)-1))
