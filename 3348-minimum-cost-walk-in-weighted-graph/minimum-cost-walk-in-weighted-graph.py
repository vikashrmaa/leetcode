from collections import defaultdict, deque
from typing import List

class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Step 1: Build adjacency list with weights
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        # Step 2: Precompute reachable components using BFS
        component = {}  # Stores the representative node of each component
        min_cost = {}   # Stores the minimum AND cost for each component
        
        def bfs(start):
            queue = deque([start])
            visited = set([start])
            comp_nodes = []
            min_and = -1  # Initialize with all bits set (0xFFFFFFFF)

            while queue:
                node = queue.popleft()
                comp_nodes.append(node)

                for neighbor, weight in graph[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
                    min_and &= weight  # Apply bitwise AND on all edges

            # Assign the same component ID and min cost to all nodes in this component
            for node in comp_nodes:
                component[node] = start
                min_cost[start] = min_and
        
        # Process all components
        for i in range(n):
            if i not in component:
                bfs(i)
        
        # Step 3: Answer queries
        answer = []
        for si, ti in query:
            if component.get(si, -1) != component.get(ti, -1):
                answer.append(-1)
            else:
                answer.append(min_cost[component[si]])
        
        return answer
