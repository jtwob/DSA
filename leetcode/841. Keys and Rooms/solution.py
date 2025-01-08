class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        visited = set()
        while len(queue) != 0:
            newRoom = queue.pop()
            if(newRoom not in visited):     
                nextRooms = rooms[newRoom]
                visited.add(newRoom)
                queue.extend(rooms[newRoom])
            
        return len(visited) == len(rooms)