class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for char in s:
            if char == '*':
                if stack:  # Remove the last character if the stack is not empty
                    stack.pop()
            else:
                stack.append(char)  # Add non-star characters to the stack
        
        return ''.join(stack)  # Join the stack into a string