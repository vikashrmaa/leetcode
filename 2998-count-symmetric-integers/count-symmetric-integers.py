class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        count = 0
        for i in range(low, high + 1):
            s = str(i)
            length = len(s)
            if length % 2 == 0:
                half = length // 2
                left_sum = sum(int(d) for d in s[:half])
                right_sum = sum(int(d) for d in s[half:])
                if left_sum == right_sum:
                    count += 1
        return count