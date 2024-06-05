class Solution(object):
    def commonChars(self, words):
        # an empty arr
        res = []
        # set all words
        word1 = set(words[0])
        # iterate word1
        for i in word1:
            # count frequency of each `char`(i) in word
            freq = min([word.count(i) for word in words])
            # multiply of each char to freq and append to res arr
            res += [i] * freq
        return res