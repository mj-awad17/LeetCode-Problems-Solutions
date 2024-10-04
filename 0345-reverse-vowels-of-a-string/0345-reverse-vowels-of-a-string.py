class Solution(object):
    def reverseVowels(self, s):
        # vowels = {'a','e','i','o','u','A','E','I','O','U'}
        # l1 = []
        # l2 = []
        # for i in range(len(s)):
        #     if s[i] in vowels:
        #         l1.append(s[i])
        #         l2.append(i)
        # for j in range(len(l2)):
        #     s = s[:l2[j]] + l1[-j-1] + s[l2[j] + 1:]
        # return s

        vowels = "aeiouAEIOU"
        l, r = 0, len(s)-1
        s = list(s)
        while l < r:
            while s[l] not in vowels and l < r:
                l += 1 
            while s[r] not in vowels and r > l:
                r -= 1
            
            temp = s[l]
            s[l] = s[r]
            s[r] = temp
            l += 1 
            r -= 1 
        return "".join(s)