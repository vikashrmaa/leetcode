class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine):
            return False 
        hashmap = {}
        for i in magazine:
            hashmap[i] = 1 + hashmap.get(i , 0)   

        for i in ransomNote:
            if hashmap.get(i, 0) == 0:
                return False
            
            hashmap[i] -= 1
        return True
          
