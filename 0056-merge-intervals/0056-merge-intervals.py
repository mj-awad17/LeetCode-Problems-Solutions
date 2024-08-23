class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals.

        Args:
            intervals (List[List[int]]): A list of intervals, where each interval is represented as a list of two integers [start, end].

        Returns:
            List[List[int]]: A list of merged intervals.
        """
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # If the list of merged intervals is empty or if the current interval does not overlap with the previous, simply append it.
            if not merged or interval[0] > merged[-1][1]:
                merged.append(interval)
            # Otherwise, there is an overlap, so we merge the current interval with the previous one.
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged