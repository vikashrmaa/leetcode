class Solution:
    def coloredCells(self, n: int) -> int:
        r = 0
        if n > 0:
            r = n**2 + (n - 1)**2
        return r