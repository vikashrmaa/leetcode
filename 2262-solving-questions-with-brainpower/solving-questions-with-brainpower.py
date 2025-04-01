class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        return (f:=cache(lambda i:i<len(q) and max(q[i][0]+f(i+q[i][1]+1),f(i+1))))(0)