class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        max_idx = max(max(seats), max(students)) + 1
        count_seats = [0] * max_idx
        count_students = [0] * max_idx

        for seat in seats:
            count_seats[seat] += 1
        for student in students:
            count_students[student] += 1
        
        i, j = 0, 0
        move = 0
        remain = len(students)
        while remain:
            if count_seats[i] == 0:
                i += 1
            if count_students[j] == 0:
                j += 1
            if count_seats[i] and count_students[j]:
                move += abs(i - j)
                count_seats[i] -= 1
                count_students[j] -= 1
                remain -= 1
        return move