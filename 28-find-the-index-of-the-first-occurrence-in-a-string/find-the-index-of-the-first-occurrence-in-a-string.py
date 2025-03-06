class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(needle)
        for i in range(len(haystack) - n + 1):  # Loop through haystack up to possible match start
            if haystack[i:i+n] == needle:  # Check substring of length 'n'
                return i  # Return index of first occurrence
        return -1  # Return -1 if needle not found
