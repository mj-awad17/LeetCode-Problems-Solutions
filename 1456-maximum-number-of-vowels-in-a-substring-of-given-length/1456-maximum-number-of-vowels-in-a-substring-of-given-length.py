class Solution:
    def maxVowels(self, s: str, k: int) -> int: 
        vowels = {'a','e','i','o','u'}
        # two pointers
        i, j = 0, 0 
        # result
        res = 0
        # iterate r in length os string s

        for r in range(len(s)): 
            # increment j when get vowel
            if s[r] in vowels:
                j += 1

            # window size
            if (r-i+1) > k:
                # decrement from j (rightside)
                if s[i] in vowels:
                    j -= 1
                # increment in i(leftside)
                i += 1
            # check max from res by j(window)
            res = max(res, j)
        return res