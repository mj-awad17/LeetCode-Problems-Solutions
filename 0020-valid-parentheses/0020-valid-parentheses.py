class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapping = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in mapping:
                # It's a closing bracket
                if not stack or stack[-1] != mapping[char]:
                    return False  # Mismatched or extra closing bracket
                stack.pop()  # Valid match found
            else:
                # It's an opening bracket
                stack.append(char)

        return not stack  # Return True if all opening brackets are matched