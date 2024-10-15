#
# CS Problems
# Leetcode
# 841. Keys and Rooms
#

class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()

        def dfs(room: int):
            # skip rooms already visited
            if room in visited:
                return
            visited.add(room)
            # recurisively visit rooms that the current room has key
            for next_room in rooms[room]:
                dfs(next_room)

        # traverse dfs to visit all rooms starting from room 0
        dfs(0)

        # check if all rooms visited
        return len(visited) == len(rooms)
