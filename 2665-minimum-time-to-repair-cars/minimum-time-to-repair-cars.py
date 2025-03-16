class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left, right = 0, min(ranks) * cars * cars
        
        def canRepairInTime(time):
            total_cars = 0
            for rank in ranks:
                total_cars += int(math.sqrt(time // rank))  # Cars this mechanic car repair
                if total_cars >= cars:  # Early stopping condition
                    return True
            return total_cars >= cars
        
        while left < right:
            mid = (left + right) // 2
            if canRepairInTime(mid):
                right = mid  # Try a smaller time
            else:
                left = mid + 1  # Increase time
            
        return left  # Minimum time needed