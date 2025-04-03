class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for c in strs:
            count = [0] * 26
            for i in c:
                count[ord(i) - ord("a")]+= 1
            res[tuple(count)].append(c)
        return list(res.values())