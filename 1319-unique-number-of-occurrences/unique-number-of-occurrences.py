class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count = Counter(arr)
        check = set()
        for i in count.values():
            if i in check:
                return False
            check.add(i)
        return True 


