class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = [0]
        visited = []
        while len(queue) != 0:
            newRoom = queue.pop()
            if(newRoom in visited):
                return False
            nextRooms = rooms[newRoom]
            visited.append(newRoom)
            for i in range(len(nextRooms)):
                queue.append(nextRooms[i])
            
        if len(visited) < len(rooms):
            return False
        else:
            return True