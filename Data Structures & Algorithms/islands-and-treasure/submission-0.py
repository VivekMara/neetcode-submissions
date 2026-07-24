from collections import deque
from typing import List

class Solution:
    def islandsAndTreasure(self, rooms: List[List[int]]) -> None:
        rows, cols = len(rooms), len(rooms[0])
        INF = 2147483647
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        q = deque()
        
        # Multi-source: push ALL gates at once
        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    q.append((r, c))
        
        # BFS
        while q:
            cr, cc = q.popleft()
            for dr, dc in dirs:
                nr, nc = cr + dr, cc + dc
                if (0 <= nr < rows and 0 <= nc < cols and 
                    rooms[nr][nc] == INF):
                    rooms[nr][nc] = rooms[cr][cc] + 1
                    q.append((nr, nc))