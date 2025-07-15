# https://leetcode.com/problems/valid-word/description/?envType=daily-question&envId=2025-07-15

class Solution:
    def isValid(self, word: str) -> bool:
        has_vowel = False
        has_cons = False
        vowels = ["a", "e", "i", "o", "u"]
        n = len(word)
        if n < 3:
            return False
        
        for c in word:

            if c.isalpha():
                if c.lower() in vowels:
                    has_vowel = True
                else:
                    has_cons = True
            
            elif not c.isdigit():
                return False
        
        return has_vowel and has_cons
        

        