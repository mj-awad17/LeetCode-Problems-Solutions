class Solution:
    def compress(self, chars: List[str]) -> int:
        # Initialize pointers and the length of the input array
        write = 0  # Pointer for writing compressed characters
        read = 0   # Pointer for reading characters
        n = len(chars)
        
        while read < n:
            current_char = chars[read]  # Character to count
            count = 0  # Count of the current character
            
            # Count the number of occurrences of the current character
            while read < n and chars[read] == current_char:
                read += 1
                count += 1
            
            # Write the current character to the compressed array
            chars[write] = current_char
            write += 1
            
            # If count is greater than 1, write the count as well
            if count > 1:
                for digit in str(count):
                    chars[write] = digit
                    write += 1
        
        # Return the new length of the compressed array
        return write
