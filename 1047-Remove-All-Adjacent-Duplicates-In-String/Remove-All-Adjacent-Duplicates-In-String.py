class Solution(object):
    def removeDuplicates(self, s):
        chars = list(s)  # Convert the string to a list of characters
        write, read = 0, 0
        
        while read < len(chars):
            if write > 0 and chars[write-1] == chars[read]:
                write -= 1
            else:
                chars[write] = chars[read]
                write += 1
            read += 1
        
        return ''.join(chars[:write])  # Convert the modified list back to a string