class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        nums_count = Counter()

        for row in grid:
            for num in row:
                nums_count[num] += 1


        a,b = -1, -1 
        for i in range(1, n * n + 1):
            if nums_count[i] == 2:
                a = i 
            elif i not in nums_count:
                b = i
        return [a, b]