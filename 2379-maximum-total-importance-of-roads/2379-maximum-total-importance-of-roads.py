class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        # Calculate the degree of each city
        count_degree = [0] * n
        for a, b in roads:
            count_degree[a] += 1
            count_degree[b] += 1
        # labeling the degrees and calculate the importance of roads
        labels, impt = 1, 0
        for count in sorted(count_degree):
            impt += labels * count
            labels += 1
        return impt