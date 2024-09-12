class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # make all the words in unique (set)
        allowed = set(allowed)

        res = len(words)
        # nested loop
        for w in words:
            for c in w:
                if c not in allowed:
                    res -= 1
                    break
        return res