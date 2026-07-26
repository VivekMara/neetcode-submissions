class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        max_area = 0
        visited = set()
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r, c) not in visited:
                    area = 0
                    stack = []
                    stack.append((r, c))
                    visited.add((r, c))
                    while stack:
                        cr, cc = stack.pop()
                        area += 1
                        for dr, dc in dirs:
                            nr, nc = cr + dr, cc + dc
                            if nr >= 0 and nr < rows and nc >= 0 and nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                visited.add((nr, nc))
                                stack.append((nr, nc))
                    max_area = max(area, max_area)
        return max_area