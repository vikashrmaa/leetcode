from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        from collections import defaultdict
        
        # Create adjacency list
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        visited = set()
        complete_components = 0
        
        def dfs(node, component):
            stack = [node]
            while stack:
                curr = stack.pop()
                if curr not in visited:
                    visited.add(curr)
                    component.add(curr)
                    stack.extend(graph[curr] - visited)
        
        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component)
                
                # Check if the component is complete
                is_complete = all(len(graph[node]) == len(component) - 1 for node in component)
                if is_complete:
                    complete_components += 1
        
        return complete_components