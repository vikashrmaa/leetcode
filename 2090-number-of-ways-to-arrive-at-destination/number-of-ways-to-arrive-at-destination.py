from heapq import heappop, heappush
from collections import defaultdict
from typing import List

class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        # Step 1: Build the graph
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append((v, time))
            graph[v].append((u, time))
        
        # Step 2: Initialize Dijkstra’s Algorithm
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        min_heap = [(0, 0)]  # (travel_time, node)
        
        while min_heap:
            current_time, node = heappop(min_heap)
            
            if current_time > dist[node]:
                continue  # Ignore outdated distances
            
            for neighbor, travel_time in graph[node]:
                new_time = current_time + travel_time
                
                # If we found a shorter path to neighbor
                if new_time < dist[neighbor]:
                    dist[neighbor] = new_time
                    ways[neighbor] = ways[node]
                    heappush(min_heap, (new_time, neighbor))
                
                # If we found another shortest path to neighbor
                elif new_time == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n - 1]
