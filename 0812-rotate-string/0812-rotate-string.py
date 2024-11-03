class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # 
        if len(s) != len(goal):
            return False
            print(s, "", goal)
        return goal in s + s