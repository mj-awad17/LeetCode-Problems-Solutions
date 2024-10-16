class Solution:
    def decodeString(self, s: str) -> str:
        # empty stack
        stack = []
        current_num = 0
        current_str = ""
        
        for char in s:
            
            if char.isdigit():
                current_num = current_num * 10 + int(char)  # Build the number
            elif char == '[':
                # Push the current number and string onto the stack
                stack.append((current_str, current_num))
                current_str = ""  # Reset current string
                current_num = 0  # Reset current number
            elif char == ']':
                # Pop from stack and build the string
                last_str, num = stack.pop()
                current_str = last_str + current_str * num
            else:
                current_str += char  # Build the current string
        
        return current_str