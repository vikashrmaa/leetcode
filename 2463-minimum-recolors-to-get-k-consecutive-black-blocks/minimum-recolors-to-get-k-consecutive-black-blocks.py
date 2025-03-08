class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        n = len(blocks)
        white = 0
        res = n
        for i in range(n):
            if blocks[i] == "W":
                white += 1
            if i - k >= 0 and blocks[i-k] == "W":
                white -= 1

            if i >= k - 1:
                res = min(res, white)

        return res

