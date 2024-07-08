class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        # Initialize a list of friends
        friends = list(range(1, n+1))
        
        # Current position in the circle
        curr = 0
        
        while len(friends) > 1:
            # Move k steps clockwise
            curr = (curr + k - 1) % len(friends)
            
            # Remove the friend at the current position
            friends.pop(curr)
        
        # The last remaining friend is the winner
        return friends[0]