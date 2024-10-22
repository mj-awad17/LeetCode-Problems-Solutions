class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        # Result to store surviving asteroids
        result = []
        
        # Iterate through each asteroid
        for a in asteroids:
            # Handle collisions for asteroids moving left
            while result and a < 0 < result[-1]:
                # Compare the absolute values to determine the outcome
                if -a > result[-1]:
                    # The asteroid in the result is destroyed
                    result.pop()
                    continue
                elif -a == result[-1]:
                    # Both asteroids are destroyed
                    result.pop()
                # If -a < result[-1], the current asteroid is destroyed
                break
            else:
                # If no collision occurred, add the asteroid to the result
                result.append(a)
        
        return result