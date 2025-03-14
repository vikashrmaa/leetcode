class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0  # Not enough candies to give each child at least one
        
        left, right = 1, max(candies)
        
        def canAllocate(mid: int) -> bool:
            count = sum(c // mid for c in candies)
            return count >= k
        
        best = 0
        while left <= right:
            mid = (left + right) // 2
            if canAllocate(mid):
                best = mid
                left = mid + 1  # Try to find a larger valid allocation
            else:
                right = mid - 1  # Reduce the search space
        
        return best