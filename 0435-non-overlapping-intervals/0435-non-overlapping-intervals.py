class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
    # Intervals ko sort karna, taaki hum unhe asaani se iterate kar sakein
        intervals.sort()

    # Ek variable res ko initialize karna, jo intervals ko remove karne ke liye zaroori hai
        res = 0

    # Ek variable prevEnd ko initialize karna, jo previous interval ke end time ko store karta hai
        prevEnd = intervals[0][1]

    # Intervals ko iterate karna, lekin humesha second interval se start karte hain (index 1 se)
        for s, e in intervals[1:]:
    # Agar current interval previous interval se overlap nahi karta hai, to:
            if s >= e:
    # Previous End ko update karna, taaki hum next interval ke liye ready ho jayein
                prevEnd = e
    # Agar current interval previous interval se overlap karta hai, to:
            elif s < prevEnd:
    # Result ko increment karna, taaki hum interval ko remove kar sakein
                res += 1
    # Previous End ko update karna, taaki hum next interval ke liye ready ho jayein
                prevEnd = min(e, prevEnd)
    # Agar current interval previous interval se overlap nahi karta hai, to:
            else:
    # Previous End ko update karna, taaki hum next interval ke liye ready ho jayein
                prevEnd = e
    # Final result ko return karna, jo intervals ko remove karne ke liye zaroori hai
        return res
