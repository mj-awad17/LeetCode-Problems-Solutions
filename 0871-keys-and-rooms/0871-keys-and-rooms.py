class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        
        visited = [False] * n
        stack = [0]
        
        visited[0] = True
        visited_count = 1
        
        while stack:
            room = stack.pop()
        
            for key in rooms[room]:
                if not visited[key]:
                    visited[key] = True
                    visited_count += 1
                    stack.append(key)
        
        return visited_count == n