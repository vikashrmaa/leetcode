class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = 0
        l = 0
        r = 0
        running_count  = 0
        total_count = 3
        hashmap= {key:0 for key in "abc"}

        while r < len(s):
            current_character = s[r]
            if hashmap[current_character] == 0:
                running_count +=1 
            hashmap[current_character] += 1

            while running_count == total_count and l<=r:
                res += len(s) - r
                hashmap[s[l]] -= 1
                if hashmap[s[l]] == 0:
                    running_count -= 1
                l += 1
            r += 1
        return res
