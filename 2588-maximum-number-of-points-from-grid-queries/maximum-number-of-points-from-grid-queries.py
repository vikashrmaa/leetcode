from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])
        result = [0] * len(queries)
        
        visited = [[False] * n for _ in range(m)]
        min_heap = [(grid[0][0], 0, 0)]  # (value, row, col)
        visited[0][0] = True
        count = 0  # Number of unique cells visited
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for index, q in sorted_queries:
            while min_heap and min_heap[0][0] < q:
                value, r, c = heapq.heappop(min_heap)
                count += 1
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < m and 0 <= nc < n and not visited[nr][nc]:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited[nr][nc] = True
            
            result[index] = count
        
        return result
