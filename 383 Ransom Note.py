class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_dict = {}

        for i in magazine:
            if i in magazine_dict:
                magazine_dict[i] += 1
            else:
                magazine_dict[i] = 1
        
        for i in ransomNote:
            if i in magazine_dict and magazine_dict[i] > 0:
                magazine_dict[i] -= 1
            else: 
                return False
            
        return True