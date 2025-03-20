class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)

        for i, n in enumerate(temperatures):
            while stack and stack[-1][0] < n:
                stackN,stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append((n, i))
        return res