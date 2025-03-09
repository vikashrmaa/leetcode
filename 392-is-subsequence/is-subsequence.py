class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0  # Pointers for s and t

        while i < len(s) and j < len(t):
            if s[i] == t[j]:  # If characters match, move `i`
                i += 1
            j += 1  # Always move `j` to check the next character in `t`

        return i == len(s)  # If `i` reaches end of `s`, it is a subsequence